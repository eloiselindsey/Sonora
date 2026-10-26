import json, random, math
from pathlib import Path
R=random.Random(44)
root=Path(__file__).resolve().parent
# Cada linha: enunciado | correta | distrator 1 | distrator 2 | distrator 3 | explicação científica
E={
'base': '''Uma oscilação completa corresponde a...|um ciclo de ida e volta até a mesma fase|somente metade de um ciclo|uma mudança definitiva de posição|uma medida de energia|Um ciclo termina ao retornar ao mesmo estado periódico de movimento.
Qual grandeza é expressa em hertz?|frequência|amplitude|distância|potência|Hz corresponde ao número de ciclos completos a cada segundo.
Um corpo realiza 10 ciclos em 2 s. A frequência é...|5 Hz|20 Hz|0,2 Hz|12 Hz|Divida o número de ciclos pelo tempo: 10/2 = 5 Hz.
Qual unidade corresponde a velocidade?|m/s|m²|W/m²|Hz|Metros por segundo indica distância percorrida por unidade de tempo.
No gráfico de posição versus tempo, a distância horizontal entre picos indica...|período|comprimento de onda|potência sonora|intensidade|Quando o eixo horizontal é o tempo, a separação entre repetições equivale ao período.''',
'ondas': '''Uma onda mecânica requer...|um meio material|ausência completa de matéria|sempre um campo elétrico|uma frequência exatamente audível|Ondas mecânicas se propagam por interações entre partes do meio.
Uma onda transversal possui oscilação...|perpendicular à direção de propagação|sempre paralela à propagação|sempre circular|sem direção definida|A classificação depende da orientação do movimento do meio em relação ao avanço da perturbação.
A distância entre duas cristas consecutivas chama-se...|comprimento de onda|período|potência|volume|Pontos consecutivos na mesma fase estão separados por λ.
A amplitude representa...|o afastamento máximo da grandeza em relação ao equilíbrio|o número de ciclos por segundo|a distância percorrida em um segundo|o tempo total da experiência|Amplitude quantifica o valor máximo da perturbação relativamente ao equilíbrio.
Uma onda eletromagnética pode...|viajar no vácuo|existir apenas na água|ser obrigatoriamente longitudinal no ar|ter frequência sempre abaixo de 20 Hz|A luz pode viajar no espaço vazio, ao contrário do som.''',
'som': '''A produção de som está relacionada principalmente a...|uma fonte que vibra|um objeto necessariamente quente|luz visível|ausência de partículas|Fontes vibrantes geram perturbações mecânicas em um meio.
No ar, ondas sonoras comuns são predominantemente...|longitudinais|transversais à propagação|eletromagnéticas|estáticas|As moléculas oscilam aproximadamente paralelas ao avanço da onda de pressão.
O som não se propaga no vácuo porque...|falta um meio material para transmitir a perturbação|sua frequência se torna zero automaticamente|o vácuo absorve todo som|o vácuo reduz a intensidade pela metade|Ondas sonoras são mecânicas e precisam de partículas interagindo.
Ultrassom apresenta frequência tipicamente...|acima de 20 kHz|sempre abaixo de 20 Hz|exatamente 440 Hz|igual a 0 Hz|Acima da faixa auditiva humana típica, frequências são classificadas como ultrassom.
Uma região de compressão de onda sonora no ar apresenta...|pressão local acima da pressão média|ausência absoluta de moléculas|luz mais forte|velocidade da luz alterada|As moléculas ficam momentaneamente mais próximas, aumentando a pressão local.''',
'propriedades': '''Sons graves geralmente têm...|frequência mais baixa|intensidade necessariamente menor|amplitude sempre nula|velocidade maior que a luz|A altura percebida de tons simples está fortemente ligada à frequência.
Um som pode ser agudo e fraco?|sim, porque altura e intensidade são propriedades diferentes|não, agudo significa alto volume|não, grave e fraco são sinônimos|sim, mas apenas no vácuo|Frequência está ligada à altura; amplitude e energia estão ligadas à intensidade.
O timbre permite distinguir...|fontes com mesma nota, mas espectros e envelopes distintos|somente sons acima de 100 dB|apenas sons de frequências diferentes|a distância total percorrida por uma onda|Harmônicos e evolução temporal influenciam a identidade sonora.
A duração de um som corresponde...|ao intervalo durante o qual ocorre o evento sonoro|necessariamente ao período de um ciclo|sempre à inversa da amplitude|à velocidade de propagação|O período é a duração de uma oscilação; duração total pode abranger muitas oscilações.
Ao aumentar a frequência de 220 para 440 Hz, mantendo condições comparáveis, a sensação esperada é...|uma nota mais aguda|uma nota necessariamente mais forte|redução da altura em uma oitava|eliminação completa do timbre|Dobrar a frequência equivale a subir uma oitava na referência musical convencional.''',
'velocidade': '''A velocidade do som no ar a aproximadamente 20 °C é próxima de...|343 m/s|3 m/s|300 000 000 m/s|10 000 km/s|O valor de 343 m/s é uma aproximação usual para ar próximo a 20 °C.
O som se propaga no vácuo?|não|sim, com a velocidade da luz|sim, apenas em frequências altas|sim, desde que seja intenso|A propagação sonora requer matéria.
Para estimar uma velocidade constante, usamos...|distância dividida por tempo|distância vezes tempo|tempo dividido pela amplitude|frequência vezes área|Velocidade v = distância/intervalo de tempo.
O que modifica a velocidade do som no ar?|temperatura e propriedades do meio|cor do objeto|volume do computador isoladamente|idioma falado|A velocidade depende das condições físicas do gás.
Vemos o relâmpago antes do trovão porque...|a luz chega muito mais rapidamente que o som|o som sempre se forma minutos depois|a luz não leva tempo para percorrer o espaço|o trovão viaja no vácuo|O som e a luz podem ser emitidos quase simultaneamente, mas suas velocidades são muito diferentes.''',
'fontes': '''Em uma corda fixa, o primeiro modo estacionário possui...|nós nas duas extremidades|um ventre obrigatório em cada extremidade|nenhuma região oscilante|frequência zero|Extremidades fixas não se deslocam e são nós de vibração.
Quando encurtamos a parte vibrante de uma corda ideal sem alterar o restante, a frequência fundamental tende a...|aumentar|diminuir|ficar sempre nula|tornar-se ultrassom obrigatoriamente|Para corda ideal, f₁ = v/(2L): menor L implica maior f₁.
Uma onda estacionária possui ventres, onde a amplitude é...|máxima no modo considerado|sempre zero|obrigatoriamente igual à frequência|uma constante de velocidade|Ventres são pontos de maior amplitude local; nós têm amplitude nula ideal.
Um tubo ideal fechado em uma ponta apresenta fundamental...|f₁ = v/(4L)|f₁ = v/L|f₁ = 4Lv|f₁ = L/v|Para uma ponta fechada e outra aberta, cabe um quarto de comprimento de onda no modo fundamental.
Ressonância é...|resposta acentuada próximo às frequências naturais de um sistema|ausência completa de vibração|som que viaja no vácuo|sinônimo de eco distante|A resposta depende da relação entre excitação e modos naturais do sistema.''',
'fenomenos': '''O eco é consequência de...|reflexão sonora|mudança química do ar|som no vácuo|absorção total da onda|A reflexão devolve parte da energia ao observador.
A refração está relacionada a...|mudanças de direção associadas à variação da velocidade no meio|sempre à perda total de frequência|ausência de propagação|subida do som em linha reta obrigatória|Variações espaciais de velocidade podem curvar ou desviar caminhos de propagação.
Quando ondas se encontram em um meio linear...|suas perturbações se somam|elas deixam de existir definitivamente|a energia sempre dobra|a frequência de todas vira zero|A superposição soma algebricamente a grandeza física considerada.
Interferência destrutiva perfeita em um ponto requer, entre outras coisas,...|perturbações de mesma magnitude e fases opostas|duas fontes com amplitude infinita|luz visível necessariamente|um meio sem partículas|Sinais opostos de igual módulo podem somar zero naquele ponto.
Batimentos podem ser ouvidos quando tons possuem...|frequências próximas|frequências sempre iguais a zero|velocidade no vácuo|pressão constante sem oscilação|Frequências próximas produzem uma modulação lenta da amplitude total.''',
'decibeis': '''A escala em decibéis é...|logarítmica|diretamente proporcional ao número de ondas|uma escala de metros|uma unidade exclusiva de distância|Os níveis resultam do logaritmo de razões de grandezas.
Um aumento de 10 dB no nível de intensidade representa...|dez vezes a intensidade física no modelo|duas vezes a intensidade sempre|mais dez watts por metro quadrado|10% a mais de frequência|A diferença é 10 log₁₀(I₂/I₁); 10 dB indica razão 10.
Ruído urbano persistente pode prejudicar...|concentração e qualidade do sono|somente o brilho dos objetos|somente as frequências ultrassônicas|a velocidade da luz|Poluição sonora influencia atividades e bem-estar mesmo antes de haver dano auditivo.
Uma demonstração digital de 100 dB numa página garante reproduzir 100 dB reais?|não, sem medição e calibração não existe essa garantia|sim, em qualquer dispositivo|sim, se usar fones|sim, se o gráfico for vermelho|Volume digital não constitui medição calibrada de pressão acústica.
O risco auditivo depende de...|nível, duração e repetição de exposição|somente da cor do ambiente|somente do nome do instrumento|apenas do valor de frequência em Hz|Orientações de saúde consideram duração e intensidade da exposição.''',
'musica': '''Uma oitava acima de 440 Hz corresponde a...|880 Hz|441 Hz|220 Hz|660 Hz|Uma oitava superior dobra a frequência.
A unidade física da frequência musical é...|hertz|litro|decibel por metro|quilograma|Frequência expressa oscilações por segundo.
Um semitom na escala temperada equivale a multiplicar a frequência por...|2^(1/12)|2|12|1/12|Doze razões iguais 2^(1/12) multiplicadas resultam em 2.
O Lá₄ de referência é frequentemente...|440 Hz|40 Hz|4 400 000 Hz|12 Hz|440 Hz é convenção frequente de afinação, com outras referências possíveis.
O timbre da mesma nota pode diferir entre instrumentos devido a...|harmônicos e envelope temporal|alteração necessária da velocidade da luz|mudança obrigatória do período de todas as ondas|frequências sempre idênticas em todo o espectro|Uma fundamental semelhante pode ter combinações harmônicas distintas.'''
}
M={
'base': '''Em um gráfico temporal, dois picos estão separados por 0,25 s. Qual é a frequência?|4 Hz|0,25 Hz|25 Hz|2 Hz|T = 0,25 s, logo f = 1/T = 4 Hz.
A velocidade de uma onda é 340 m/s. Em 2 segundos, a frente percorre...|680 m|170 m|342 m|0,0059 m|Com velocidade constante, distância = v × t = 340 × 2 = 680 m.
Uma fonte vibra 90 vezes em 3 segundos. Qual é seu período?|1/30 s|30 s|3 s|270 s|A frequência é 90/3 = 30 Hz; período T = 1/30 s.
Qual alternativa interpreta corretamente um gráfico pressão × posição?|a distância entre picos sucessivos corresponde a λ|a separação entre picos equivale sempre a um segundo|amplitude é obrigatoriamente a velocidade|posição é medida em Hz|Em eixo de posição, a repetição espacial define λ, não T.
Por que log₁₀(1000) = 3?|porque 10³ = 1000|porque 1000/10 = 3|porque 10 × 3 = 1000|porque 1000 tem três algarismos significativos|O logaritmo informa qual expoente torna 10 igual ao argumento.''',
'ondas': '''Uma onda de frequência 100 Hz e velocidade 300 m/s apresenta λ...|3 m|30 000 m|0,33 m|300 Hz|λ = v/f = 300/100 = 3 m.
Mantida a velocidade de propagação, dobrar a frequência faz λ...|cair pela metade|dobrar|ficar quatro vezes maior|ir a zero necessariamente|Em v = λf com v fixo, λ é inversamente proporcional a f.
Uma onda avança horizontalmente e o meio vibra verticalmente. Ela é...|transversal|longitudinal|necessariamente ultrassônica|impossível|O sentido da oscilação é perpendicular ao sentido da propagação.
Duas cristas consecutivas aparecem em x = 1 m e x = 5 m. Qual λ?|4 m|6 m|5 m|1 m|Comprimento de onda é 5 − 1 = 4 m.
Uma mesma fonte passa a emitir maior amplitude mantendo frequência. O que permanece igual, se o meio não mudar?|período da onda|energia transportada necessariamente|amplitude|intensidade sempre|A frequência fixa determina T = 1/f, independentemente dessa mudança de amplitude.''',
'som': '''Por que o som no ar pode ser desenhado como senoide mesmo sendo longitudinal?|o gráfico pode representar pressão em função da posição|as moléculas percorrem trajetórias senoidais no espaço|a onda se torna eletromagnética|o som abandona o meio material|A curva pode ser uma representação de pressão, não do trajeto das partículas.
Em uma região de rarefação, a pressão local é...|menor que a média|sempre exatamente zero|maior que em uma compressão|independente da vibração|Rarefações são regiões de menor pressão relativa.
Se a fonte vibra, mas a câmara é evacuada, o som externo tende a diminuir porque...|há menos partículas disponíveis para transmitir a onda|a frequência da fonte se torna negativa|a luz deixa de existir|o objeto não pode se mover|A onda necessita de acoplamento mecânico com um meio.
Qual comparação é fisicamente correta?|luz viaja no vácuo, som não|ambos sempre precisam de ar|som sempre viaja mais rápido que luz|som não passa pela água|Ondas eletromagnéticas não exigem meio material; as mecânicas exigem.
Um evento de 10 Hz corresponde a...|infrassom na classificação humana típica|ultrassom|um tom sempre audível a todos|luz visível|10 Hz está abaixo dos cerca de 20 Hz do limite inferior típico de audição humana.''',
'propriedades': '''Uma flauta e um violão tocam 440 Hz em volume próximo. O que explica a diferença perceptível?|timbre ligado a harmônicos e envelope|a fundamental é obrigatoriamente diferente|a velocidade do som se torna maior no violão|um dos instrumentos não gera ondas|Notas de mesma fundamental podem ter espectros e envoltórias diferentes.
Se um tom de 440 Hz muda para 880 Hz, mas o ganho digital é conservado, qual característica física muda claramente?|frequência associada à altura|densidade do ar necessariamente|distância da fonte|duração obrigatoriamente|Dobrar f eleva a altura em uma oitava no contexto musical.
A intensidade física em condições apropriadas é descrita por...|potência dividida por área|frequência dividida por período|massa multiplicada por tempo|diâmetro dividido pela tensão|I = P/A para potência acústica atravessando área apropriada.
Um tom dura 3 s e vibra a 200 Hz. Qual distinção está correta?|3 s é duração e 0,005 s é período|3 s é o período|200 s é duração|a frequência é 3 Hz|T = 1/200 = 0,005 s, enquanto o evento total dura 3 s.
Por que um som com maior amplitude de pressão não precisa ter altura maior?|a altura relaciona-se sobretudo à frequência, não à amplitude|a amplitude é uma medida de hertz|o período sempre dobra|não há relação entre pressão e som|Amplitude participa da intensidade em condições definidas; frequência participa da altura.''',
'velocidade': '''A 10 °C, pela aproximação v ≈ 331 + 0,6θ, a velocidade é...|337 m/s|3310 m/s|343 m/s|6 m/s|331 + 0,6 × 10 = 337 m/s.
Um trovão chega 6 s depois do relâmpago. A cerca de 340 m/s, a distância é...|2040 m|340 m|56,7 m|4080 km|d ≈ v t = 340 × 6 = 2040 m.
Ao entrar em região onde a velocidade é menor, mantendo f, λ...|diminui|aumenta|fica necessariamente idêntico|torna-se uma medida de tempo|λ = v/f, então velocidade menor com f fixa implica λ menor.
Que propriedade adicional à densidade influencia fortemente velocidade em materiais?|rigidez ou compressibilidade|cor da superfície|massa total do observador|volume digital do celular|Velocidade de perturbações mecânicas depende de inércia e resposta elástica.
Qual situação é melhor aproximada pela lei do inverso do quadrado?|fonte pontual isotrópica em campo livre|sala altamente reverberante|onda guiada em tubo estreito ideal|som no vácuo|I ∝ 1/r² pressupõe distribuição esférica e ausência de perdas extras.''',
'fontes': '''Uma corda ideal de 1 m com v = 200 m/s tem frequência fundamental de...|100 Hz|200 Hz|400 Hz|50 Hz|f₁ = v/(2L) = 200/(2×1) = 100 Hz.
Se quadruplicarmos a tensão da corda ideal, com μ e L constantes, a frequência fundamental...|dobra|quadruplica|cai pela metade|fica zero|v = √(F/μ); quadruplicar F duplica v e também f₁.
Um tubo aberto de 0,5 m com v = 340 m/s tem fundamental...|340 Hz|170 Hz|680 Hz|85 Hz|f₁ = v/(2L) = 340/(2×0,5) = 340 Hz.
Um tubo fechado-aberto ideal apresenta quais múltiplos da fundamental?|1, 3, 5, 7,...|1, 2, 3, 4,...|0, 2, 4,...|somente o segundo|As condições de contorno permitem somente n ímpar.
Qual mudança tende a reduzir a frequência fundamental de uma corda ideal?|aumentar o comprimento L|aumentar a tensão F|reduzir a massa por comprimento μ|aumentar a velocidade v|f₁ = v/(2L), portanto aumentar L reduz f₁ se v for mantida.''',
'fenomenos': '''Um eco retorna em 0,5 s em ar com v = 340 m/s. A parede está a...|85 m|170 m|680 m|340 m|Percurso de ida e volta: d = vt/2 = 340×0,5/2 = 85 m.
Duas ondas de mesma amplitude e frequência chegam com diferença de fase π. O resultado ideal pode ser...|cancelamento naquele ponto|reforço máximo sempre|alteração da velocidade da luz|mudança permanente da frequência das fontes|Ondas de fase oposta têm perturbações instantâneas opostas.
Para uma onda atravessando uma interface estacionária, o que geralmente se mantém?|frequência|comprimento de onda|velocidade de propagação|ângulo de direção|A frequência é imposta pela fonte; velocidade e λ podem mudar.
Dois sinais de 440 e 442 Hz produzem batimentos em torno de...|2 Hz|882 Hz|440 Hz|220 Hz|fᵦ = |442 − 440| = 2 Hz.
Qual ação aumenta a absorção acústica, em geral?|instalar materiais adequados para dissipar energia acústica|aumentar toda reflexão|remover o meio material de uma sala sem alterar o resto|somar dB aritmeticamente|Materiais absorventes dissipam parte da energia incidente, reduzindo certas reflexões.''',
'decibeis': '''Se uma intensidade sonora aumenta 100 vezes, a mudança de nível é...|20 dB|100 dB|2 dB|10 000 dB|10 log₁₀(100) = 20 dB.
Para I = 10⁻⁹ W/m² e I₀ = 10⁻¹² W/m², o nível é...|30 dB|3 dB|90 dB|0 dB|I/I₀ = 10³; β = 10×3 = 30 dB.
O som A mede 60 dB e o B 70 dB, nas mesmas condições de referência. B tem...|10 vezes a intensidade física de A|10 vezes mais frequência|apenas 10% mais intensidade|100 vezes menos intensidade|Diferença de +10 dB corresponde à razão de intensidade 10.
Qual afirmação sobre fones e segurança é mais adequada?|nível e duração de exposição importam|apenas a frequência da música determina risco|qualquer som acima de 60 dB causa lesão imediata|sons graves são sempre seguros|Riscos de audição variam com dose e susceptibilidade individual.
Por que dBA é diferente de um nível genérico dB de intensidade?|dBA usa ponderação por frequência em medidas sonoras|dBA é medida de distância|dBA elimina todo ruído|dBA é sinônimo de hertz|A ponderação A relaciona-se à sensibilidade auditiva conforme a frequência e aplica-se a medições práticas.''',
'musica': '''Uma nota de 220 Hz tem oitava superior de...|440 Hz|110 Hz|221 Hz|330 Hz|A oitava superior dobra a frequência: 220×2=440 Hz.
Na afinação justa, uma quinta de razão 3:2 acima de 200 Hz tem...|300 Hz|400 Hz|133,3 Hz|1200 Hz|200×3/2 = 300 Hz na afinação justa.
Quantos semitons temperados equivalem a uma oitava?|12|6|8|24 Hz|O sistema de temperamento igual divide a oitava em 12 semitons.
Se n = −12 na fórmula temperada, f₂ é...|metade de f₁|o dobro de f₁|f₁ menos 12 Hz|f₁ elevado ao quadrado|2^(−12/12)=1/2, uma oitava descendente.
Dois sinais de 440 e 880 Hz representam, em termos de frequências fundamentais,...|uma oitava|um uníssono|uma diferença de 1 semitom|um batimento de 1 Hz|A razão 880/440 = 2 caracteriza uma oitava.'''
}
def parse(d,level):
  out=[]
  for mod, raw in d.items():
    for ln in raw.split('\n'):
      seg=ln.strip().split('|',5)
      assert len(seg)==6,(mod,seg)
      question,good,*rest=seg
      wrong=rest[:3]; why=rest[3]
      opts=[good]+wrong
      R.shuffle(opts)
      out.append(dict(module=mod,level=level,type='choice',question=question,options=opts,answer=opts.index(good),explanation=why))
  return out
questions=parse(E,'facil')+parse(M,'medio')
assert len(questions)==90
# 30 novos problemas avançados em situações variadas, respostas numéricas reais e resolução.
def num(mod,text,result,solution,tol=.02,formula=''):
  questions.append(dict(module=mod,level='dificil',type='number',question=text,answer=round(float(result),5),tolerance=tol,explanation=solution,formula=formula))
num('base','Uma vibração completa 840 ciclos em 3,5 s. Informe a frequência (Hz).',240,'f = ciclos/tempo = 840/3,5 = 240 Hz.',.001,'freq')
num('base','Um período dura 2,5 ms. Determine a frequência (Hz).',400,'Converta 2,5 ms = 0,0025 s; f = 1/T = 400 Hz.',.001,'freq')
num('base','O som percorre 1,7 km em 5 s. Determine a velocidade média (m/s).',340,'Converta 1,7 km = 1700 m; v = 1700/5 = 340 m/s.',.001,'velocidade')
num('ondas','Uma onda de 160 Hz viaja a 320 m/s. Calcule seu comprimento de onda (m).',2,'λ = v/f = 320/160 = 2 m.',.001,'onda')
num('ondas','Uma onda periódica apresenta λ = 0,85 m e f = 400 Hz. Determine v (m/s).',340,'v = λf = 0,85×400 = 340 m/s.',.001,'onda')
num('ondas','Em um gráfico espacial, a distância entre a primeira e a sexta crista consecutiva é 7,5 m. Qual λ (m)?',1.5,'Entre seis cristas existem cinco intervalos: λ = 7,5/5 = 1,5 m.',.001,'onda')
num('som','O tímpano recebe um tom periódico a 125 Hz durante 4 s. Aproximadamente quantos ciclos chegam nesse período?',500,'Número de ciclos N = f×t = 125×4 = 500.',.001,'freq')
num('som','Um sinal tem frequência fundamental de 750 Hz. Quantas oscilações completas ocorrem em 0,08 s?',60,'N = f t = 750×0,08 = 60.',.001,'freq')
num('som','O período de uma vibração sonora é 0,002 s. Qual frequência (Hz)?',500,'f = 1/0,002 = 500 Hz.',.001,'freq')
num('propriedades','Uma fonte isotrópica ideal fornece 12 W em área atravessada de 6 m². Calcule a intensidade média (W/m²).',2,'I = P/A = 12/6 = 2 W/m²; trata-se de distribuição uniforme ideal.',.001,'intensidade')
num('propriedades','Uma fonte pontual ideal produz intensidade 24 unidades a 2 m. Qual intensidade (mesmas unidades) a 4 m?',6,'I₂ = I₁(r₁/r₂)² = 24(2/4)² = 6. Modelo ideal em campo livre.',.001,'esfera')
num('propriedades','Um som dura 2,4 segundos e tem frequência de 250 Hz. Quantos ciclos ocorrem?',600,'N = f×duração = 250×2,4 = 600 ciclos.',.001,'freq')
num('velocidade','Com ar seco a 25 °C, use v ≈ 331 + 0,6θ. Determine v (m/s).',346,'v ≈ 331 + 0,6×25 = 346 m/s.',.001,'temperatura')
num('velocidade','Um raio é visto e 4,5 s depois se ouve o trovão. A 340 m/s, estime a distância (m).',1530,'d = v×t = 340×4,5 = 1530 m. Tempo da luz foi desprezado.',.001,'velocidade')
num('velocidade','Uma onda mantém f = 250 Hz, mas passa a viajar a 1500 m/s em outro material. Determine λ (m).',6,'λ = v/f = 1500/250 = 6 m. Frequência mantida na interface estacionária.',.001,'onda')
num('fontes','Corda ideal sob tensão F = 100 N e μ = 0,01 kg/m: determine v (m/s).',100,'v = √(F/μ) = √(100/0,01) = √10000 = 100 m/s.',.001,'corda')
num('fontes','Corda ideal fixa de L = 0,8 m e v = 320 m/s: calcule o terceiro harmônico (Hz).',600,'f₃ = 3v/(2L) = 960/1,6 = 600 Hz.',.001,'corda')
num('fontes','Tubo ideal fechado-aberto de L = 0,25 m e v = 340 m/s: calcule o terceiro harmônico permitido (Hz), n=3.',1020,'f₃ = 3×340/(4×0,25) = 1020 Hz. Somente n ímpares são permitidos.',.001,'tubo')
num('fontes','Tubo ideal aberto de comprimento 0,4 m e v = 320 m/s: determine a frequência fundamental (Hz).',400,'f₁ = v/(2L) = 320/(0,8) = 400 Hz.',.001,'tubo')
num('fenomenos','O eco volta após 0,75 s. Para v = 344 m/s, determine a distância até a parede (m).',129,'d = vt/2 = 344×0,75/2 = 129 m.',.001,'eco')
num('fenomenos','Dois tons estão em 512 Hz e 518 Hz. Qual é a frequência de batimentos (Hz)?',6,'fᵦ = |518−512| = 6 Hz.',.001,'batimento')
num('fenomenos','Duas ondas possuem pressões instantâneas de 0,12 Pa e −0,035 Pa. Encontre a perturbação resultante (Pa).',.085,'Superposição linear: 0,12 + (−0,035) = 0,085 Pa.',.0001,'soma')
num('fenomenos','Uma onda de 425 Hz muda de meio com v = 340 m/s para outro com v = 255 m/s. Qual o novo λ (m)?',.6,'f permanece 425 Hz; λ₂ = 255/425 = 0,6 m.',.001,'onda')
num('decibeis','Uma intensidade é 10⁻⁵ W/m². Adote I₀ = 10⁻¹² W/m². Qual o nível em dB?',70,'I/I₀ = 10⁷ e β = 10×log₁₀(10⁷) = 70 dB.',.001,'db')
num('decibeis','Dois sinais comparáveis diferem por 30 dB no nível de intensidade. Quantas vezes maior é a intensidade do maior?',1000,'I₂/I₁ = 10^(30/10) = 10³ = 1000.',.001,'difdb')
num('decibeis','Uma intensidade passa de 2×10⁻⁸ para 2×10⁻⁶ W/m². Qual a variação de nível (dB)?',20,'Razão = 100; Δβ = 10 log₁₀(100) = 20 dB.',.001,'difdb')
num('decibeis','Uma intensidade de 10⁻⁹ W/m² aumenta 10 vezes. Qual será o nível (dB) em relação a I₀ = 10⁻¹² W/m²?',40,'I nova = 10⁻⁸; razão 10⁴; β = 40 dB.',.001,'db')
num('musica','Na escala temperada, suba 12 semitons a partir de 523,25 Hz. Determine a nova frequência (Hz).',1046.5,'f₂ = 523,25×2^(12/12) = 1046,5 Hz.',.005,'intervalo')
num('musica','Na escala temperada, desça 24 semitons a partir de 880 Hz. Determine a frequência (Hz).',220,'2^(−24/12)=1/4; f₂ = 880/4 = 220 Hz.',.001,'intervalo')
num('musica','Uma quinta justa em afinação justa usa razão 3:2. Partindo de 256 Hz, qual a frequência acima (Hz)?',384,'f₂ = 256×3/2 = 384 Hz.',.001,'intervalo')

# Atividades alternativas reais: verdadeiro/falso, sequenciar e associar conceitos.
TF={
'base':('O período de uma oscilação é medido em segundos.',True,'O período expressa a duração de um ciclo; sua unidade no SI é o segundo.'),
'ondas':('Uma onda mecânica consegue propagar-se pelo vácuo perfeito.',False,'Ondas mecânicas precisam das interações de um meio material.'),
'som':('No ar, o som comum se propaga por variações locais de pressão.',True,'Compressões e rarefações se deslocam, enquanto as partículas oscilam ao redor do equilíbrio.'),
'propriedades':('Um som agudo é obrigatoriamente mais intenso do que um grave.',False,'Agudo se refere à frequência; intensidade é outra grandeza.'),
'velocidade':('A velocidade do som é universalmente igual a 343 m/s em qualquer material.',False,'343 m/s é um valor típico no ar próximo de 20 °C; outros meios têm outras velocidades.'),
'fontes':('Numa corda ideal de extremidades fixas, as pontas são nós de vibração.',True,'Extremidades fixas não se deslocam no modelo de ondas estacionárias.'),
'fenomenos':('O tempo medido de um eco simples inclui ida e volta da onda.',True,'Por isso d = vt/2 para a distância até a parede.'),
'decibeis':('Dez decibéis adicionais significam que a intensidade física cresceu apenas dez por cento.',False,'Diferença de +10 dB significa razão de intensidades 10, na mesma referência.'),
'musica':('Uma oitava acima corresponde ao dobro da frequência fundamental.',True,'O intervalo de oitava relaciona frequências na razão 2:1.')}
ORDER={
'base':('Ordene as etapas para calcular a frequência a partir de ciclos e tempo.',['Identificar quantidade de ciclos N e tempo t','Converter o tempo para segundos','Calcular f = N/t','Expressar o resultado em hertz'],'Frequência é ciclos divididos pelo tempo em segundos.'),
'ondas':('Organize o cálculo do comprimento de onda usando velocidade e frequência.',['Identificar a velocidade v e frequência f','Conferir as unidades m/s e Hz','Isolar λ = v/f','Calcular λ em metros'],'Use v = λf e isole λ antes de substituir valores.'),
'som':('Organize a explicação de como o som chega ao ouvido.',['A fonte vibra','O meio apresenta variações de pressão','A onda se propaga pelo meio','O tímpano recebe a perturbação'],'O som mecânico depende da vibração e propagação até o ouvido.'),
'propriedades':('Ordene um procedimento para comparar dois timbres com a mesma nota.',['Escolher a mesma frequência fundamental','Produzir dois espectros harmônicos diferentes','Ouvir em volume digital baixo','Comparar as formas de onda e envelopes'],'Timbre envolve harmônicos e envelope, mesmo sem alterar a fundamental.'),
'velocidade':('Ordene o procedimento para estimar a distância de um trovão.',['Medir tempo entre o clarão e o trovão','Escolher velocidade aproximada do som no ar','Usar d ≈ vt','Expressar a distância com unidade'],'Desprezamos o tempo da luz em distâncias cotidianas e usamos d ≈ vt.'),
'fontes':('Organize o cálculo da fundamental de uma corda ideal fixa.',['Identificar tensão F e densidade linear μ','Calcular v = √(F/μ)','Medir o comprimento L','Calcular f₁ = v/(2L)'],'A velocidade na corda vem de F/μ e o modo fundamental é v/(2L).'),
'fenomenos':('Ordene a investigação da reflexão numa parede.',['Identificar fonte, observador e refletor','Medir o intervalo entre o som e o eco','Calcular o percurso total vt','Dividir por dois para achar a distância à parede'],'Em eco simples a trajetória total tem dois trechos.'),
'decibeis':('Ordene o cálculo de diferença de níveis a partir de intensidades.',['Obter duas intensidades comparáveis','Calcular a razão I₂/I₁','Encontrar o logaritmo decimal da razão','Multiplicar por dez para obter Δβ em dB'],'Diferença = 10 log₁₀(I₂/I₁).'),
'musica':('Organize a descoberta de uma nota n semitons acima de outra.',['Identificar a frequência inicial f₁','Contar o número de semitons n','Calcular o fator 2^(n/12)','Multiplicar f₁ pelo fator'],'No temperamento igual cada semitom representa a mesma razão multiplicativa.')}
MATCH={
'base':('Associe unidades e grandezas.', [('Hertz','frequência'),('Segundo','período'),('Metro por segundo','velocidade')],'As unidades SI distinguem ciclos por segundo, tempo e distância por tempo.'),
'ondas':('Associe os elementos de uma onda.', [('Amplitude','afastamento máximo'),('Período','duração de um ciclo'),('Comprimento de onda','separação espacial de fases equivalentes')],'Amplitude, período e comprimento de onda descrevem aspectos distintos.'),
'som':('Relacione os fenômenos acústicos básicos.', [('Compressão','pressão acima da média'),('Rarefação','pressão abaixo da média'),('Vácuo','ausência de meio para som mecânico')],'O som no ar envolve variações de pressão no meio material.'),
'propriedades':('Associe propriedades e percepções.', [('Altura','grave ou agudo'),('Intensidade percebida','forte ou fraco'),('Timbre','identidade da fonte sonora')],'Altura, volume percebido e timbre não devem ser confundidos.'),
'velocidade':('Associe condições e resultados típicos.', [('Ar a 20 °C','velocidade próxima de 343 m/s'),('Água','velocidade típica perto de 1480 m/s'),('Vácuo','sem propagação de som mecânico')],'Os valores são aproximados e dependem de temperatura e material.'),
'fontes':('Associe componentes das ondas estacionárias.', [('Nó','deslocamento mínimo'),('Ventre','deslocamento máximo'),('Fundamental','modo de menor frequência permitida')],'Nós e ventres descrevem o padrão estacionário; a fundamental é o primeiro modo.'),
'fenomenos':('Associe cada fenômeno à sua descrição.', [('Reflexão','retorno da onda'),('Refração','mudança de caminho por velocidade'),('Interferência','reforço ou cancelamento pela soma')],'Os fenômenos têm causas e consequências físicas distintas.'),
'decibeis':('Associe diferenças de nível e razões de intensidade.', [('+10 dB','razão 10'),('+20 dB','razão 100'),('+30 dB','razão 1000')],'Para nível de intensidade, razão = 10^(Δβ/10).'),
'musica':('Associe intervalos e razões ideais.', [('Oitava','2:1'),('Quinta justa em afinação justa','3:2'),('Quarta justa em afinação justa','4:3')],'As razões simples citadas referem-se a afinação justa, exceto a oitava, universal à comparação.')}
for mod,(statement,correct,explain) in TF.items():
 idx=next(i for i,q in enumerate(questions) if q['module']==mod and q['level']=='facil')
 questions[idx]=dict(module=mod,level='facil',type='truefalse',question=statement,options=['Verdadeiro','Falso'],answer=0 if correct else 1,explanation=explain)
for mod,(question,steps,explain) in ORDER.items():
 idx=next(i for i,q in enumerate(questions) if q['module']==mod and q['level']=='medio')
 shuffled=steps.copy();R.shuffle(shuffled)
 if shuffled==steps:shuffled=steps[1:]+steps[:1]
 questions[idx]=dict(module=mod,level='medio',type='order',question=question,steps=shuffled,correctOrder=steps,answer=None,explanation=explain)
for mod,(question,pairs,explain) in MATCH.items():
 idx=next(i for i,q in enumerate(questions) if q['module']==mod and q['level']=='medio' and q['type']=='choice')
 options=[right for left,right in pairs];R.shuffle(options)
 questions[idx]=dict(module=mod,level='medio',type='match',question=question,pairs=[dict(left=left,right=right) for left,right in pairs],matchOptions=options,answer=None,explanation=explain)

assert len(questions)==120, len(questions)
assert {lvl:sum(q['level']==lvl for q in questions) for lvl in ('facil','medio','dificil')}=={'facil':45,'medio':45,'dificil':30}
for i,q in enumerate(questions):
  q['id']=f'q{i+1:03d}'
  q['hints']=[f"Identifique o conceito central: {q['module']}.", 'Procure a relação entre as grandezas antes de calcular.', 'Confira unidades e releia a explicação da aula correspondente.']
  if q['type']=='number':
    q['hints']=['Liste os dados do problema e a grandeza pedida.','Identifique a fórmula da situação e converta as unidades.','Substitua os números e confira a ordem das operações.']
(root/'questions.json').write_text(json.dumps(questions,ensure_ascii=False,indent=2))
flash_groups={
'ondas':[
('O que é uma onda?','Perturbação que se propaga transportando energia sem transportar matéria globalmente.'),
('Por que o som é onda mecânica?','Porque necessita da interação entre partículas de um meio material.'),
('O que mede a amplitude?','O afastamento máximo da grandeza oscilante em relação ao equilíbrio.'),
('O que significa 250 Hz?','250 ciclos completos em cada segundo.'),
('Qual é a relação entre f e T?','f = 1/T e T = 1/f.'),
('Como calcular v de onda periódica?','v = λf, com λ em metros e f em hertz.'),
('Transversal e longitudinal: diferença?','Na transversal o meio oscila perpendicularmente à propagação; na longitudinal, paralelamente.'),
('A luz precisa de ar para se propagar?','Não; ondas eletromagnéticas podem viajar no vácuo.')],
'propriedades':[
('O que é altura sonora?','Sensação ligada principalmente à frequência: grave ou agudo.'),
('O que distingue som forte de fraco?','A sensação de volume relaciona-se à intensidade e ao ouvido, não simplesmente à altura.'),
('O que caracteriza o timbre?','Espectro harmônico e envelope temporal ajudam a identificar fontes.'),
('Aumentar amplitude eleva necessariamente a frequência?','Não. São grandezas independentes em muitos modelos.'),
('Por que uma flauta e violão diferem na mesma nota?','Porque seus harmônicos e envelopes sonoros são distintos.'),
('O que é duração?','O tempo total do evento sonoro, diferente do período de um ciclo.'),
('O que muda ao dobrar 440 para 880 Hz?','A altura sobe aproximadamente uma oitava no sistema musical convencional.'),
('Como a intensidade ideal se relaciona à potência?','I = P/A para potência transmitida pela área considerada.')],
'decibeis':[
('O que significa +10 dB em intensidade?','Dez vezes mais intensidade física no modelo comparável.'),
('A escala em dB é linear?','Não, é logarítmica.'),
('Como expressar nível de intensidade?','β = 10 log₁₀(I/I₀), usualmente I₀ = 10⁻¹² W/m² no contexto didático.'),
('O que diferencia dBA?','Ponderação de frequência em medição prática de pressão sonora.'),
('O que determina risco auditivo?','Nível, duração, repetição e condições pessoais e ambientais.'),
('Som alto no site é sonômetro calibrado?','Não; áudio digital não é medição acústica calibrada.')],
'velocidade':[
('Velocidade aproximada do som a 20 °C?','343 m/s no ar, como estimativa didática.'),
('Som viaja mais rápido na água ou no ar, em condições usuais?','Na água, mas velocidade depende das propriedades dos meios.'),
('Como estimar v no ar seco perto do ambiente?','v ≈ 331 + 0,6θ (m/s), com θ em °C.'),
('O que ocorre com λ se v muda e f se mantém?','λ muda na mesma proporção que v, pois v = λf.'),
('Por que a luz do raio chega antes do trovão?','A luz propaga-se muito mais rapidamente que o som.'),
('Qual relação descreve velocidade média?','v = Δs/Δt, com unidades coerentes.')],
'fontes':[
('Qual relação vale para a corda ideal?','v = √(F/μ), com tensão F e densidade linear μ.'),
('Onde ficam nós em uma corda fixa?','Nas extremidades fixas, que não se deslocam.'),
('Frequência fundamental da corda ideal?','f₁ = v/(2L).'),
('Tubo fechado-aberto ideal: quais harmônicos?','Apenas múltiplos ímpares da fundamental.'),
('Uma oitava acima dobra o quê?','A frequência fundamental.'),
('Na escala temperada, qual fórmula?','f₂ = f₁ × 2^(n/12), com n em semitons.')],
'fenomenos':[
('Por que d = vt/2 no eco?','Porque o som percorre o trecho até a parede duas vezes.'),
('O que é refração sonora?','Mudança de direção associada a diferenças de velocidade do meio.'),
('O que diz a superposição linear?','A perturbação resultante é a soma algébrica das perturbações.'),
('Quando ocorre interferência destrutiva ideal?','Quando duas perturbações de mesma magnitude chegam com fases opostas.'),
('Como calcular batimentos?','fᵦ = |f₁−f₂| para dois tons próximos.'),
('Absorção e isolamento são a mesma coisa?','Não. Absorção dissipa parte da energia; isolamento busca reduzir a transmissão.')]
}
flash=[]
for mod,rows in flash_groups.items():
 for question,answer in rows:
  flash.append(dict(id=f'f{len(flash)+1:02d}',module=mod,front=question,back=answer))
assert len(flash)==40
(root/'flashcards.json').write_text(json.dumps(flash,ensure_ascii=False,indent=2))
print('Questions',len(questions),'Flashcards',len(flash))
