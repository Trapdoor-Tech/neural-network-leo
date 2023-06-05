program neural_network.aleo{
struct S11{
w100: i64, w110: i64, w120: i64, w130: i64, w140: i64, w150: i64, w160: i64, w170: i64, w101: i64, w111: i64, w121: i64, w131: i64, w141: i64, w151: i64, w161: i64, w171: i64, w102: i64, w112: i64, w122: i64, w132: i64, w142: i64, w152: i64, w162: i64, w172: i64, w103: i64, w113: i64, w123: i64, w133: i64, w143: i64, w153: i64, w163: i64, w173: i64,
}
struct S21{
w200: i64, w210: i64, w220: i64, w230: i64, w201: i64, w211: i64, w221: i64, w231: i64, w202: i64, w212: i64, w222: i64, w232: i64, w203: i64, w213: i64, w223: i64, w233: i64,
}
struct S31{
w300: i64, w310: i64, w320: i64, w330: i64, w301: i64, w311: i64, w321: i64, w331: i64, w302: i64, w312: i64, w322: i64, w332: i64, w303: i64, w313: i64, w323: i64, w333: i64, w304: i64, w314: i64, w324: i64, w334: i64, w305: i64, w315: i64, w325: i64, w335: i64,
}
struct S4{
input0: i64,input1: i64,input2: i64,input3: i64,input4: i64,input5: i64,input6: i64,input7: i64,
}
struct B1{
b10: i64, b11: i64, b12: i64, b13: i64, b20: i64, b21: i64, b22: i64, b23: i64, b30: i64, b31: i64, b32: i64, b33: i64, b34: i64, b35: i64,
}
struct Res{
 r0: i64, r1: i64, r2: i64, r3: i64, r4: i64, r5: i64,
}
transition main(s11:S11,s21:S21,s31:S31,s4:S4,b1:B1) ->Res{
let neuron00: i64 = s4.input0;
let neuron01: i64 = s4.input1;
let neuron02: i64 = s4.input2;
let neuron03: i64 = s4.input3;
let neuron04: i64 = s4.input4;
let neuron05: i64 = s4.input5;
let neuron06: i64 = s4.input6;
let neuron07: i64 = s4.input7;
let neuron10: i64 = rectified_linear_activation(neuron00 * s11.w100 / 1000000i64  + neuron01 * s11.w110 / 1000000i64  + neuron02 * s11.w120 / 1000000i64  + neuron03 * s11.w130 / 1000000i64  + neuron04 * s11.w140 / 1000000i64  + neuron05 * s11.w150 / 1000000i64  + neuron06 * s11.w160 / 1000000i64  + neuron07 * s11.w170 / 1000000i64  + b1.b10);
let neuron11: i64 = rectified_linear_activation(neuron00 * s11.w101 / 1000000i64  + neuron01 * s11.w111 / 1000000i64  + neuron02 * s11.w121 / 1000000i64  + neuron03 * s11.w131 / 1000000i64  + neuron04 * s11.w141 / 1000000i64  + neuron05 * s11.w151 / 1000000i64  + neuron06 * s11.w161 / 1000000i64  + neuron07 * s11.w171 / 1000000i64  + b1.b11);
let neuron12: i64 = rectified_linear_activation(neuron00 * s11.w102 / 1000000i64  + neuron01 * s11.w112 / 1000000i64  + neuron02 * s11.w122 / 1000000i64  + neuron03 * s11.w132 / 1000000i64  + neuron04 * s11.w142 / 1000000i64  + neuron05 * s11.w152 / 1000000i64  + neuron06 * s11.w162 / 1000000i64  + neuron07 * s11.w172 / 1000000i64  + b1.b12);
let neuron13: i64 = rectified_linear_activation(neuron00 * s11.w103 / 1000000i64  + neuron01 * s11.w113 / 1000000i64  + neuron02 * s11.w123 / 1000000i64  + neuron03 * s11.w133 / 1000000i64  + neuron04 * s11.w143 / 1000000i64  + neuron05 * s11.w153 / 1000000i64  + neuron06 * s11.w163 / 1000000i64  + neuron07 * s11.w173 / 1000000i64  + b1.b13);
let neuron20: i64 = rectified_linear_activation(neuron10 * s21.w200 / 1000000i64  + neuron11 * s21.w210 / 1000000i64  + neuron12 * s21.w220 / 1000000i64  + neuron13 * s21.w230 / 1000000i64  + b1.b20);
let neuron21: i64 = rectified_linear_activation(neuron10 * s21.w201 / 1000000i64  + neuron11 * s21.w211 / 1000000i64  + neuron12 * s21.w221 / 1000000i64  + neuron13 * s21.w231 / 1000000i64  + b1.b21);
let neuron22: i64 = rectified_linear_activation(neuron10 * s21.w202 / 1000000i64  + neuron11 * s21.w212 / 1000000i64  + neuron12 * s21.w222 / 1000000i64  + neuron13 * s21.w232 / 1000000i64  + b1.b22);
let neuron23: i64 = rectified_linear_activation(neuron10 * s21.w203 / 1000000i64  + neuron11 * s21.w213 / 1000000i64  + neuron12 * s21.w223 / 1000000i64  + neuron13 * s21.w233 / 1000000i64  + b1.b23);
let neuron30: i64 = neuron20 * s31.w300 / 1000000i64  + neuron21 * s31.w310 / 1000000i64  + neuron22 * s31.w320 / 1000000i64  + neuron23 * s31.w330 / 1000000i64  + b1.b30;
let neuron31: i64 = neuron20 * s31.w301 / 1000000i64  + neuron21 * s31.w311 / 1000000i64  + neuron22 * s31.w321 / 1000000i64  + neuron23 * s31.w331 / 1000000i64  + b1.b31;
let neuron32: i64 = neuron20 * s31.w302 / 1000000i64  + neuron21 * s31.w312 / 1000000i64  + neuron22 * s31.w322 / 1000000i64  + neuron23 * s31.w332 / 1000000i64  + b1.b32;
let neuron33: i64 = neuron20 * s31.w303 / 1000000i64  + neuron21 * s31.w313 / 1000000i64  + neuron22 * s31.w323 / 1000000i64  + neuron23 * s31.w333 / 1000000i64  + b1.b33;
let neuron34: i64 = neuron20 * s31.w304 / 1000000i64  + neuron21 * s31.w314 / 1000000i64  + neuron22 * s31.w324 / 1000000i64  + neuron23 * s31.w334 / 1000000i64  + b1.b34;
let neuron35: i64 = neuron20 * s31.w305 / 1000000i64  + neuron21 * s31.w315 / 1000000i64  + neuron22 * s31.w325 / 1000000i64  + neuron23 * s31.w335 / 1000000i64  + b1.b35;
let res:Res = Res{
 r0:neuron30, r1:neuron31, r2:neuron32, r3:neuron33, r4:neuron34, r5:neuron35,
};
 return res;
}
function rectified_linear_activation(x: i64) -> i64 {
let result: i64 = 0i64;
if x > 0i64 {
result = x;
}
return result;
}
}