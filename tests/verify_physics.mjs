/* node --experimental-default-type=module tests/verify_physics.mjs */
import assert from 'node:assert/strict';
import {labDefinitions,computeLab} from '../js/labs.js';
import {modules,lessons,formulae} from '../js/content.js';
const close=(v,w,eps=1e-8)=>assert.ok(Math.abs(v-w)<eps,`${v} != ${w}`);
assert.equal(modules.length,9);
assert.equal(lessons.length,37);
assert.equal(formulae.length,14);
assert.equal(labDefinitions.length,14);
for (const l of labDefinitions){
 const p=Object.fromEntries(l.controls.map(x=>[x[0],x[5]]));
 const a=computeLab(l.id,p);
 assert.ok(a.headline&&a.detail&&a.conclusion,'Faltam resultados em '+l.id);
 assert.ok(!/NaN|Infinity|undefined/.test(JSON.stringify(a)),'Resultados inválidos em '+l.id);
}
assert.match(computeLab('ondas',{f:200,a:1,v:340}).headline,/1,7 m/);
assert.match(computeLab('eco',{d:68,a:15,v:340}).headline,/0,4 s/);
assert.match(computeLab('batimentos',{f1:440,delta:4}).headline,/4 batimento/);
assert.match(computeLab('decibeis',{db1:40,db2:60}).detail,/100/);
assert.match(computeLab('intervalos',{f1:440,n:12}).headline,/880/);
assert.match(computeLab('trovao',{d:3430,temp:20}).headline,/10 s/);
console.log('PASS: 9 módulos, 37 aulas, 14 fórmulas, 14 laboratórios e cálculos físicos de referência.');
