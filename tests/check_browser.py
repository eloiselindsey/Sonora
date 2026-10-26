import json,re,time
from pathlib import Path
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parents[1]
html=(P/'index.html').read_text()
html=html.replace('<link rel="stylesheet" href="./css/style.css">','').replace('<script type="module" src="./js/app.js"></script>','')
css=(P/'css/style.css').read_text()
content=(P/'js/content.js').read_text().replace('export ','')
labs=(P/'js/labs.js').read_text().replace('export ','')
app=(P/'js/app.js').read_text()
app=re.sub(r'^import .*?;\s*','',app,flags=re.MULTILINE)
app=app[:app.index("Promise.all([fetch(")]
questions=json.loads((P/'data/questions.json').read_text())
flash=json.loads((P/'data/flashcards.json').read_text())
code=content+'\n'+labs+'\n'+app+'\n'+f'D.questions={json.dumps(questions,ensure_ascii=False)};D.flashcards={json.dumps(flash,ensure_ascii=False)};boot();'
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 pg=browser.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
 errors=[]
 pg.on('pageerror',lambda e:errors.append(str(e)))
 pg.set_content(html,wait_until='domcontentloaded')
 pg.add_style_tag(content=css)
 pg.add_script_tag(content=code)
 pg.wait_for_timeout(300)
 print('DEBUG main=',pg.locator('main').inner_text()[:300],'errors',errors, 'console?', pg.evaluate('typeof boot'))
 print('h1',pg.locator('main h1').first.inner_text(timeout=3000))
 print('cards',pg.locator('.module-card').count())
 pg.screenshot(path=str(P/'tests/preview-desktop.png'),animations='disabled')
 for route in ['aprender','modulo/ondas','aula/ondas-5','laboratorio','lab/ondas','lab/somar','lab/altura','lab/intensidade','lab/timbre','lab/corrida','lab/eco','lab/refracao','lab/superposicao','lab/batimentos','lab/decibeis','lab/instrumentos','lab/intervalos','lab/trovao','cartoes','exercicios','progresso','formulas','intensivao','roteiro/15','roteiro/30','roteiro/60','referencias','diagnostico']:
  pg.evaluate("r => { location.hash='#'+r; dispatchEvent(new HashChangeEvent('hashchange')); }",route)
  pg.wait_for_timeout(40)
  assert pg.locator('#main').inner_text().strip(),route
  print(route,pg.locator('.page-title h1').first.inner_text()[:50] if pg.locator('.page-title h1').count() else pg.locator('main').inner_text()[:30])
  if route.startswith('lab/'):
   assert pg.locator('#lab-result strong').count()==1,route
   assert pg.locator('canvas').count()==1,route
 pg.evaluate("location.hash='#lab/ondas';dispatchEvent(new HashChangeEvent('hashchange'))")
 v1=pg.locator('#lab-result strong').inner_text()
 pg.locator('[data-labcontrol="f"]').fill('8')
 v2=pg.locator('#lab-result strong').inner_text()
 print('LAB_VALUES',v1,v2)
 assert v1 != v2
 pg.screenshot(path=str(P/'tests/preview-laboratorio.png'),animations='disabled')
 pg.locator('[data-action="reset-lab"]').click()
 assert 'λ = 3 m' in pg.locator('#lab-result strong').inner_text()
 pg.evaluate("location.hash='#lab/altura';dispatchEvent(new HashChangeEvent('hashchange'))")
 pg.locator('[data-action="play-audio"]').click()
 pg.wait_for_timeout(250)
 pg.locator('[data-action="stop-audio"]').click()
 assert not errors, errors
 print('AUDIO trigger/stop passed')
 pg.locator('#theme-button').click()
 assert pg.locator('body').get_attribute('class')=='dark'
 pg.locator('#theme-button').click()
 print('THEME toggle passed')

 pg.evaluate("location.hash='#cartoes';dispatchEvent(new HashChangeEvent('hashchange'))")
 pg.locator('#flash-card').click()
 assert pg.locator('#flash-card').get_attribute('class').find('flipped')!=-1
 pg.locator('[data-action="rate-flash"][data-value="mastered"]').click()
 print('FLASH rating ok')
 pg.evaluate("location.hash='#exercicios';dispatchEvent(new HashChangeEvent('hashchange'))")
 pg.locator('[data-action="start-quiz"][data-value="10"]').click()
 pg.locator('[data-action="hint"]').click()
 assert pg.locator('.hint-box').count()==1
 if pg.locator('input[type="radio"]').count():pg.locator('input[type="radio"]').first.check()
 elif pg.locator('select[data-matchindex]').count():pg.locator('select[data-matchindex]').first.select_option(index=1)
 elif pg.locator('[data-action="move-order"]').count():pg.locator('[data-action="move-order"]:not([disabled])').first.click()
 elif pg.locator('#numeric-answer').count():pg.locator('#numeric-answer').fill('25')
 pg.locator('[data-action="check-answer"]').click()
 assert pg.locator('.feedback').count()==1
 print('QUIZ feedback',pg.locator('.feedback strong').inner_text())
 # Exercícios por tipo: cartão, ordenação, associação, numérico e V/F
 for typ in ['choice','truefalse','order','match','number']:
  pg.evaluate("ty => { let q=D.questions.find(x=>x.type===ty);quiz={ids:[q.id],index:0,answer:null,checked:false,results:[],hint:0,mode:'teste'};location.hash='#quiz';render(); }",typ)
  assert pg.locator('.quiz-question').count()==1,typ
  if typ in ['choice','truefalse']:pg.locator('input[type="radio"]').first.check()
  if typ=='order':pg.locator('[data-action="move-order"]:not([disabled])').first.click()
  if typ=='match':
   for z in pg.locator('select[data-matchindex]').all():z.select_option(index=1)
  if typ=='number':pg.locator('#numeric-answer').fill('1,75')
  pg.locator('[data-action="check-answer"]').click()
  assert pg.locator('.feedback').count()==1,typ
  print('format',typ,'passed')
 pg.evaluate("location.hash='#aula/base-1';dispatchEvent(new HashChangeEvent('hashchange'))")
 pg.locator('[data-action="complete-lesson"]').click()
 assert 'Aula concluída' in pg.locator('main').inner_text()
 print('LESSON complete ok')
 print('PAGE_ERRORS:',errors)
 assert not errors,errors
 mobile=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
 mobile_errors=[]
 mobile.on('pageerror',lambda e:mobile_errors.append(str(e)))
 mobile.set_content(html,wait_until='domcontentloaded')
 mobile.add_style_tag(content=css)
 mobile.add_script_tag(content=code)
 mobile.wait_for_timeout(200)
 mobile.screenshot(path=str(P/'tests/preview-mobile.png'),animations='disabled')
 print('mobile overflow:',mobile.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth'))
 assert mobile.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')<=1
 mobile.locator('#menu-button').click()
 assert 'open' in mobile.locator('#sidebar').get_attribute('class')
 print('MOBILE errors',mobile_errors)
 assert not mobile_errors
 browser.close()
print('ALL PASS')
