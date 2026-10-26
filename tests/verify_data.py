"""Validação do banco didático; execute python tests/verify_data.py."""
import json,math
from collections import Counter
from pathlib import Path
p=Path(__file__).resolve().parents[1]
q=json.loads((p/'data/questions.json').read_text(encoding='utf-8'))
f=json.loads((p/'data/flashcards.json').read_text(encoding='utf-8'))
assert len(q)==120, f'Questões encontradas: {len(q)}'
assert len(f)==40, f'Cartões encontrados: {len(f)}'
assert Counter(x['level'] for x in q)=={'facil':45,'medio':45,'dificil':30}
assert Counter(x['module'] for x in f)=={'ondas':8,'propriedades':8,'decibeis':6,'velocidade':6,'fontes':6,'fenomenos':6}
assert len(set(x['id'] for x in q))==len(q)
assert len(set(x['question'] for x in q))==len(q)
assert len(set(x['id'] for x in f))==len(f)
assert all(x['explanation'] and x['question'] and len(x['hints'])==3 for x in q)
for x in q:
 t=x['type']
 assert t in ('choice','truefalse','number','order','match')
 if t in ('choice','truefalse'):
  assert len(x['options'])>=2 and len(set(x['options']))==len(x['options'])
  assert isinstance(x['answer'],int) and 0<=x['answer']<len(x['options'])
 if t=='number':
  assert math.isfinite(x['answer']) and x['tolerance']>=0
 if t=='order':
  assert sorted(x['steps'])==sorted(x['correctOrder'])
 if t=='match':
  assert sorted(x['matchOptions'])==sorted(p['right'] for p in x['pairs'])
print('PASS: 120 questões; 40 flashcards; gabaritos estruturados; 5 formatos; IDs únicos.')
print('Distribuição por formato:',dict(Counter(x['type'] for x in q)))
