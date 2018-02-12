#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_9054 = ref_278 # MOV operation
ref_9513 = ref_9054 # MOV operation
ref_9531 = ((ref_9513 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_9538 = ref_9531 # MOV operation
ref_13805 = ref_278 # MOV operation
ref_14753 = ref_13805 # MOV operation
ref_14763 = (ref_14753 >> (0x35 & 0x3F)) # SHR operation
ref_14770 = ref_14763 # MOV operation
ref_15305 = ref_9538 # MOV operation
ref_15311 = ref_14770 # MOV operation
ref_15313 = (ref_15311 | ref_15305) # OR operation
ref_16294 = ref_15313 # MOV operation
ref_16304 = (ref_16294 >> (0x1 & 0x3F)) # SHR operation
ref_16311 = ref_16304 # MOV operation
ref_20335 = ref_16311 # MOV operation
ref_25016 = ref_20335 # MOV operation
ref_25614 = ref_25016 # MOV operation
ref_25630 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_25614)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_29553 = ref_278 # MOV operation
ref_30545 = ref_29553 # MOV operation
ref_30555 = ((((0x0) << 64 | ref_30545) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_31019 = ref_30555 # MOV operation
ref_31033 = ref_25630 # MOV operation
ref_31035 = ((ref_31019 - ref_31033) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_31043 = ref_31035 # MOV operation
ref_35189 = ref_31043 # MOV operation
ref_39298 = ref_278 # MOV operation
ref_40270 = ref_39298 # MOV operation
ref_40278 = ((0x9919884 + ref_40270) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_44381 = ref_35189 # MOV operation
ref_45441 = ref_44381 # MOV operation
ref_45451 = (ref_45441 >> (0x7 & 0x3F)) # SHR operation
ref_45458 = ref_45451 # MOV operation
ref_46437 = ref_45458 # MOV operation
ref_46447 = (ref_46437 >> (0x2 & 0x3F)) # SHR operation
ref_46454 = ref_46447 # MOV operation
ref_47462 = ref_46454 # MOV operation
ref_47470 = (0x7 & ref_47462) # AND operation
ref_48488 = ref_47470 # MOV operation
ref_48496 = (0x1 | ref_48488) # OR operation
ref_49046 = ref_40278 # MOV operation
ref_49052 = ref_48496 # MOV operation
ref_49054 = (ref_49052 & 0xFFFFFFFF) # MOV operation
ref_49056 = (ref_49046 >> ((ref_49054 & 0xFF) & 0x3F)) # SHR operation
ref_49063 = ref_49056 # MOV operation
ref_53272 = ref_49063 # MOV operation
ref_57144 = ref_278 # MOV operation
ref_58176 = ref_57144 # MOV operation
ref_58184 = ((0x1E5EA08F8 + ref_58176) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_62391 = ref_58184 # MOV operation
ref_72588 = ref_53272 # MOV operation
ref_78857 = ref_53272 # MOV operation
ref_79835 = ref_78857 # MOV operation
ref_79843 = (0x3F & ref_79835) # AND operation
ref_80280 = ref_79843 # MOV operation
ref_80298 = ((ref_80280 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_80305 = ref_80298 # MOV operation
ref_80808 = ref_72588 # MOV operation
ref_80814 = ref_80305 # MOV operation
ref_80816 = (ref_80814 | ref_80808) # OR operation
ref_86438 = ref_80816 # MOV operation
ref_97636 = ref_86438 # MOV operation
ref_102319 = ref_35189 # MOV operation
ref_103305 = ref_102319 # MOV operation
ref_103315 = (ref_103305 >> (0x2 & 0x3F)) # SHR operation
ref_103322 = ref_103315 # MOV operation
ref_104310 = ref_103322 # MOV operation
ref_104318 = (0xF & ref_104310) # AND operation
ref_105436 = ref_104318 # MOV operation
ref_105444 = (0x1 | ref_105436) # OR operation
ref_109447 = ref_20335 # MOV operation
ref_109963 = ref_109447 # MOV operation
ref_109977 = ref_105444 # MOV operation
ref_109979 = (ref_109977 & 0xFFFFFFFF) # MOV operation
ref_109981 = ((ref_109963 << ((ref_109979 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_109988 = ref_109981 # MOV operation
ref_114073 = ref_20335 # MOV operation
ref_118228 = ref_35189 # MOV operation
ref_119300 = ref_118228 # MOV operation
ref_119310 = (ref_119300 >> (0x2 & 0x3F)) # SHR operation
ref_119317 = ref_119310 # MOV operation
ref_120312 = ref_119317 # MOV operation
ref_120320 = (0xF & ref_120312) # AND operation
ref_121351 = ref_120320 # MOV operation
ref_121359 = (0x1 | ref_121351) # OR operation
ref_122380 = ref_121359 # MOV operation
ref_122382 = ((0x40 - ref_122380) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_122390 = ref_122382 # MOV operation
ref_122849 = ref_114073 # MOV operation
ref_122855 = ref_122390 # MOV operation
ref_122857 = (ref_122855 & 0xFFFFFFFF) # MOV operation
ref_122859 = (ref_122849 >> ((ref_122857 & 0xFF) & 0x3F)) # SHR operation
ref_122866 = ref_122859 # MOV operation
ref_123417 = ref_109988 # MOV operation
ref_123423 = ref_122866 # MOV operation
ref_123425 = (ref_123423 | ref_123417) # OR operation
ref_124356 = ref_123425 # MOV operation
ref_124364 = (0x7 & ref_124356) # AND operation
ref_124888 = ref_124364 # MOV operation
ref_124906 = ((ref_124888 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_124913 = ref_124906 # MOV operation
ref_125449 = ref_97636 # MOV operation
ref_125455 = ref_124913 # MOV operation
ref_125457 = (ref_125455 | ref_125449) # OR operation
ref_129569 = ref_125457 # MOV operation
ref_134173 = ref_20335 # MOV operation
ref_138246 = ref_35189 # MOV operation
ref_139228 = ref_138246 # MOV operation
ref_139238 = (ref_139228 >> (0x3 & 0x3F)) # SHR operation
ref_139245 = ref_139238 # MOV operation
ref_140231 = ref_139245 # MOV operation
ref_140239 = (0xF & ref_140231) # AND operation
ref_141262 = ref_140239 # MOV operation
ref_141270 = (0x1 | ref_141262) # OR operation
ref_141810 = ref_134173 # MOV operation
ref_141816 = ref_141270 # MOV operation
ref_141818 = (ref_141816 & 0xFFFFFFFF) # MOV operation
ref_141820 = (ref_141810 >> ((ref_141818 & 0xFF) & 0x3F)) # SHR operation
ref_141827 = ref_141820 # MOV operation
ref_145971 = ref_35189 # MOV operation
ref_146939 = ref_145971 # MOV operation
ref_146949 = (ref_146939 >> (0x3 & 0x3F)) # SHR operation
ref_146956 = ref_146949 # MOV operation
ref_148012 = ref_146956 # MOV operation
ref_148020 = (0xF & ref_148012) # AND operation
ref_149063 = ref_148020 # MOV operation
ref_149071 = (0x1 | ref_149063) # OR operation
ref_150070 = ref_149071 # MOV operation
ref_150072 = ((0x40 - ref_150070) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_150080 = ref_150072 # MOV operation
ref_154129 = ref_20335 # MOV operation
ref_154604 = ref_154129 # MOV operation
ref_154618 = ref_150080 # MOV operation
ref_154620 = (ref_154618 & 0xFFFFFFFF) # MOV operation
ref_154622 = ((ref_154604 << ((ref_154620 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_154629 = ref_154622 # MOV operation
ref_155160 = ref_141827 # MOV operation
ref_155166 = ref_154629 # MOV operation
ref_155168 = (ref_155166 | ref_155160) # OR operation
ref_159297 = ref_129569 # MOV operation
ref_163354 = ref_62391 # MOV operation
ref_164263 = ref_163354 # MOV operation
ref_164273 = (ref_164263 >> (0x4 & 0x3F)) # SHR operation
ref_164280 = ref_164273 # MOV operation
ref_165344 = ref_164280 # MOV operation
ref_165352 = (0xF & ref_165344) # AND operation
ref_166391 = ref_165352 # MOV operation
ref_166399 = (0x1 | ref_166391) # OR operation
ref_166837 = ref_159297 # MOV operation
ref_166843 = ref_166399 # MOV operation
ref_166845 = (ref_166843 & 0xFFFFFFFF) # MOV operation
ref_166847 = (ref_166837 >> ((ref_166845 & 0xFF) & 0x3F)) # SHR operation
ref_166854 = ref_166847 # MOV operation
ref_171069 = ref_62391 # MOV operation
ref_172125 = ref_171069 # MOV operation
ref_172135 = (ref_172125 >> (0x4 & 0x3F)) # SHR operation
ref_172142 = ref_172135 # MOV operation
ref_173166 = ref_172142 # MOV operation
ref_173174 = (0xF & ref_173166) # AND operation
ref_174097 = ref_173174 # MOV operation
ref_174105 = (0x1 | ref_174097) # OR operation
ref_175188 = ref_174105 # MOV operation
ref_175190 = ((0x40 - ref_175188) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_175198 = ref_175190 # MOV operation
ref_179180 = ref_129569 # MOV operation
ref_179655 = ref_179180 # MOV operation
ref_179669 = ref_175198 # MOV operation
ref_179671 = (ref_179669 & 0xFFFFFFFF) # MOV operation
ref_179673 = ((ref_179655 << ((ref_179671 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_179680 = ref_179673 # MOV operation
ref_180133 = ref_166854 # MOV operation
ref_180139 = ref_179680 # MOV operation
ref_180141 = (ref_180139 | ref_180133) # OR operation
ref_180689 = ref_155168 # MOV operation
ref_180695 = ref_180141 # MOV operation
ref_180697 = ((ref_180689 - ref_180695) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_180699 = ((((ref_180689 ^ (ref_180695 ^ ref_180697)) ^ ((ref_180689 ^ ref_180697) & (ref_180689 ^ ref_180695))) >> 63) & 0x1) # Carry flag
ref_180703 = (0x1 if (ref_180697 == 0x0) else 0x0) # Zero flag
ref_180705 = ((((ref_180695 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (((~(ref_180699) & 0x1) & (~(ref_180703) & 0x1)) == 0x1) else 0x0)) # SETA operation
ref_180707 = (ref_180705 & 0xFF) # MOVZX operation
ref_181191 = (ref_180707 & 0xFFFFFFFF) # MOV operation
ref_181193 = ((ref_181191 & 0xFFFFFFFF) & (ref_181191 & 0xFFFFFFFF)) # TEST operation
ref_181198 = (0x1 if (ref_181193 == 0x0) else 0x0) # Zero flag
ref_181200 = (0x1F07 if (ref_181198 == 0x1) else 0x1EDD) # Program Counter


if (ref_181198 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_9054 = ref_278 # MOV operation
    ref_9513 = ref_9054 # MOV operation
    ref_9531 = ((ref_9513 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_9538 = ref_9531 # MOV operation
    ref_13805 = ref_278 # MOV operation
    ref_14753 = ref_13805 # MOV operation
    ref_14763 = (ref_14753 >> (0x35 & 0x3F)) # SHR operation
    ref_14770 = ref_14763 # MOV operation
    ref_15305 = ref_9538 # MOV operation
    ref_15311 = ref_14770 # MOV operation
    ref_15313 = (ref_15311 | ref_15305) # OR operation
    ref_16294 = ref_15313 # MOV operation
    ref_16304 = (ref_16294 >> (0x1 & 0x3F)) # SHR operation
    ref_16311 = ref_16304 # MOV operation
    ref_20335 = ref_16311 # MOV operation
    ref_25016 = ref_20335 # MOV operation
    ref_25614 = ref_25016 # MOV operation
    ref_25630 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_25614)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_29553 = ref_278 # MOV operation
    ref_30545 = ref_29553 # MOV operation
    ref_30555 = ((((0x0) << 64 | ref_30545) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_31019 = ref_30555 # MOV operation
    ref_31033 = ref_25630 # MOV operation
    ref_31035 = ((ref_31019 - ref_31033) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_31043 = ref_31035 # MOV operation
    ref_35189 = ref_31043 # MOV operation
    ref_39298 = ref_278 # MOV operation
    ref_40270 = ref_39298 # MOV operation
    ref_40278 = ((0x9919884 + ref_40270) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_44381 = ref_35189 # MOV operation
    ref_45441 = ref_44381 # MOV operation
    ref_45451 = (ref_45441 >> (0x7 & 0x3F)) # SHR operation
    ref_45458 = ref_45451 # MOV operation
    ref_46437 = ref_45458 # MOV operation
    ref_46447 = (ref_46437 >> (0x2 & 0x3F)) # SHR operation
    ref_46454 = ref_46447 # MOV operation
    ref_47462 = ref_46454 # MOV operation
    ref_47470 = (0x7 & ref_47462) # AND operation
    ref_48488 = ref_47470 # MOV operation
    ref_48496 = (0x1 | ref_48488) # OR operation
    ref_49046 = ref_40278 # MOV operation
    ref_49052 = ref_48496 # MOV operation
    ref_49054 = (ref_49052 & 0xFFFFFFFF) # MOV operation
    ref_49056 = (ref_49046 >> ((ref_49054 & 0xFF) & 0x3F)) # SHR operation
    ref_49063 = ref_49056 # MOV operation
    ref_53272 = ref_49063 # MOV operation
    ref_57144 = ref_278 # MOV operation
    ref_58176 = ref_57144 # MOV operation
    ref_58184 = ((0x1E5EA08F8 + ref_58176) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_62391 = ref_58184 # MOV operation
    ref_72588 = ref_53272 # MOV operation
    ref_78857 = ref_53272 # MOV operation
    ref_79835 = ref_78857 # MOV operation
    ref_79843 = (0x3F & ref_79835) # AND operation
    ref_80280 = ref_79843 # MOV operation
    ref_80298 = ((ref_80280 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_80305 = ref_80298 # MOV operation
    ref_80808 = ref_72588 # MOV operation
    ref_80814 = ref_80305 # MOV operation
    ref_80816 = (ref_80814 | ref_80808) # OR operation
    ref_86438 = ref_80816 # MOV operation
    ref_97636 = ref_86438 # MOV operation
    ref_102319 = ref_35189 # MOV operation
    ref_103305 = ref_102319 # MOV operation
    ref_103315 = (ref_103305 >> (0x2 & 0x3F)) # SHR operation
    ref_103322 = ref_103315 # MOV operation
    ref_104310 = ref_103322 # MOV operation
    ref_104318 = (0xF & ref_104310) # AND operation
    ref_105436 = ref_104318 # MOV operation
    ref_105444 = (0x1 | ref_105436) # OR operation
    ref_109447 = ref_20335 # MOV operation
    ref_109963 = ref_109447 # MOV operation
    ref_109977 = ref_105444 # MOV operation
    ref_109979 = (ref_109977 & 0xFFFFFFFF) # MOV operation
    ref_109981 = ((ref_109963 << ((ref_109979 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_109988 = ref_109981 # MOV operation
    ref_114073 = ref_20335 # MOV operation
    ref_118228 = ref_35189 # MOV operation
    ref_119300 = ref_118228 # MOV operation
    ref_119310 = (ref_119300 >> (0x2 & 0x3F)) # SHR operation
    ref_119317 = ref_119310 # MOV operation
    ref_120312 = ref_119317 # MOV operation
    ref_120320 = (0xF & ref_120312) # AND operation
    ref_121351 = ref_120320 # MOV operation
    ref_121359 = (0x1 | ref_121351) # OR operation
    ref_122380 = ref_121359 # MOV operation
    ref_122382 = ((0x40 - ref_122380) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_122390 = ref_122382 # MOV operation
    ref_122849 = ref_114073 # MOV operation
    ref_122855 = ref_122390 # MOV operation
    ref_122857 = (ref_122855 & 0xFFFFFFFF) # MOV operation
    ref_122859 = (ref_122849 >> ((ref_122857 & 0xFF) & 0x3F)) # SHR operation
    ref_122866 = ref_122859 # MOV operation
    ref_123417 = ref_109988 # MOV operation
    ref_123423 = ref_122866 # MOV operation
    ref_123425 = (ref_123423 | ref_123417) # OR operation
    ref_124356 = ref_123425 # MOV operation
    ref_124364 = (0x7 & ref_124356) # AND operation
    ref_124888 = ref_124364 # MOV operation
    ref_124906 = ((ref_124888 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_124913 = ref_124906 # MOV operation
    ref_125449 = ref_97636 # MOV operation
    ref_125455 = ref_124913 # MOV operation
    ref_125457 = (ref_125455 | ref_125449) # OR operation
    ref_129569 = ref_125457 # MOV operation
    ref_185905 = ref_35189 # MOV operation
    ref_190399 = ref_35189 # MOV operation
    ref_191433 = ref_190399 # MOV operation
    ref_191441 = (0xF & ref_191433) # AND operation
    ref_191959 = ref_191441 # MOV operation
    ref_191977 = ((ref_191959 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_191984 = ref_191977 # MOV operation
    ref_192421 = ref_185905 # MOV operation
    ref_192427 = ref_191984 # MOV operation
    ref_192429 = (ref_192427 | ref_192421) # OR operation
    ref_196604 = ref_192429 # MOV operation
    ref_200688 = ref_20335 # MOV operation
    ref_205269 = ref_129569 # MOV operation
    ref_209374 = ref_196604 # MOV operation
    ref_209901 = ref_205269 # MOV operation
    ref_209907 = ref_209374 # MOV operation
    ref_209909 = (ref_209907 & ref_209901) # AND operation
    ref_210864 = ref_209909 # MOV operation
    ref_210872 = (0x1F & ref_210864) # AND operation
    ref_211368 = ref_210872 # MOV operation
    ref_211386 = ((ref_211368 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_211393 = ref_211386 # MOV operation
    ref_212006 = ref_200688 # MOV operation
    ref_212012 = ref_211393 # MOV operation
    ref_212014 = (ref_212012 | ref_212006) # OR operation
    ref_216011 = ref_212014 # MOV operation
    ref_220487 = ref_62391 # MOV operation
    ref_224531 = ref_129569 # MOV operation
    ref_225142 = ref_224531 # MOV operation
    ref_225156 = ref_220487 # MOV operation
    ref_225158 = (((sx(0x40, ref_225156) * sx(0x40, ref_225142)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_229148 = ref_216011 # MOV operation
    ref_233170 = ref_196604 # MOV operation
    ref_233691 = ref_229148 # MOV operation
    ref_233697 = ref_233170 # MOV operation
    ref_233699 = (ref_233697 | ref_233691) # OR operation
    ref_234198 = ref_233699 # MOV operation
    ref_234212 = ref_225158 # MOV operation
    ref_234214 = (((sx(0x40, ref_234212) * sx(0x40, ref_234198)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_238396 = ref_234214 # MOV operation
    ref_239440 = ref_238396 # MOV operation
    ref_239442 = ref_239440 # MOV operation
    endb = ref_239442


else:
    ref_239762 = SymVar_0
    ref_239777 = ref_239762 # MOV operation
    ref_248285 = ref_239777 # MOV operation
    ref_248778 = ref_248285 # MOV operation
    ref_248796 = ((ref_248778 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_248803 = ref_248796 # MOV operation
    ref_252789 = ref_239777 # MOV operation
    ref_253792 = ref_252789 # MOV operation
    ref_253802 = (ref_253792 >> (0x35 & 0x3F)) # SHR operation
    ref_253809 = ref_253802 # MOV operation
    ref_254248 = ref_248803 # MOV operation
    ref_254254 = ref_253809 # MOV operation
    ref_254256 = (ref_254254 | ref_254248) # OR operation
    ref_255289 = ref_254256 # MOV operation
    ref_255299 = (ref_255289 >> (0x1 & 0x3F)) # SHR operation
    ref_255306 = ref_255299 # MOV operation
    ref_259591 = ref_255306 # MOV operation
    ref_264148 = ref_259591 # MOV operation
    ref_264577 = ref_264148 # MOV operation
    ref_264593 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_264577)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_268581 = ref_239777 # MOV operation
    ref_269650 = ref_268581 # MOV operation
    ref_269660 = ((((0x0) << 64 | ref_269650) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_270144 = ref_269660 # MOV operation
    ref_270158 = ref_264593 # MOV operation
    ref_270160 = ((ref_270144 - ref_270158) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_270168 = ref_270160 # MOV operation
    ref_274320 = ref_270168 # MOV operation
    ref_278336 = ref_239777 # MOV operation
    ref_279396 = ref_278336 # MOV operation
    ref_279404 = ((0x9919884 + ref_279396) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_283524 = ref_274320 # MOV operation
    ref_284450 = ref_283524 # MOV operation
    ref_284460 = (ref_284450 >> (0x7 & 0x3F)) # SHR operation
    ref_284467 = ref_284460 # MOV operation
    ref_285507 = ref_284467 # MOV operation
    ref_285517 = (ref_285507 >> (0x2 & 0x3F)) # SHR operation
    ref_285524 = ref_285517 # MOV operation
    ref_286613 = ref_285524 # MOV operation
    ref_286621 = (0x7 & ref_286613) # AND operation
    ref_287594 = ref_286621 # MOV operation
    ref_287602 = (0x1 | ref_287594) # OR operation
    ref_288117 = ref_279404 # MOV operation
    ref_288123 = ref_287602 # MOV operation
    ref_288125 = (ref_288123 & 0xFFFFFFFF) # MOV operation
    ref_288127 = (ref_288117 >> ((ref_288125 & 0xFF) & 0x3F)) # SHR operation
    ref_288134 = ref_288127 # MOV operation
    ref_292226 = ref_288134 # MOV operation
    ref_296338 = ref_239777 # MOV operation
    ref_297368 = ref_296338 # MOV operation
    ref_297376 = ((0x1E5EA08F8 + ref_297368) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_301514 = ref_297376 # MOV operation
    ref_311709 = ref_292226 # MOV operation
    ref_317788 = ref_292226 # MOV operation
    ref_318814 = ref_317788 # MOV operation
    ref_318822 = (0x3F & ref_318814) # AND operation
    ref_319344 = ref_318822 # MOV operation
    ref_319362 = ((ref_319344 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_319369 = ref_319362 # MOV operation
    ref_319828 = ref_311709 # MOV operation
    ref_319834 = ref_319369 # MOV operation
    ref_319836 = (ref_319834 | ref_319828) # OR operation
    ref_325506 = ref_319836 # MOV operation
    ref_336747 = ref_325506 # MOV operation
    ref_341366 = ref_274320 # MOV operation
    ref_342411 = ref_341366 # MOV operation
    ref_342421 = (ref_342411 >> (0x2 & 0x3F)) # SHR operation
    ref_342428 = ref_342421 # MOV operation
    ref_343372 = ref_342428 # MOV operation
    ref_343380 = (0xF & ref_343372) # AND operation
    ref_344376 = ref_343380 # MOV operation
    ref_344384 = (0x1 | ref_344376) # OR operation
    ref_348536 = ref_259591 # MOV operation
    ref_349053 = ref_348536 # MOV operation
    ref_349067 = ref_344384 # MOV operation
    ref_349069 = (ref_349067 & 0xFFFFFFFF) # MOV operation
    ref_349071 = ((ref_349053 << ((ref_349069 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_349078 = ref_349071 # MOV operation
    ref_353287 = ref_259591 # MOV operation
    ref_357364 = ref_274320 # MOV operation
    ref_358272 = ref_357364 # MOV operation
    ref_358282 = (ref_358272 >> (0x2 & 0x3F)) # SHR operation
    ref_358289 = ref_358282 # MOV operation
    ref_359362 = ref_358289 # MOV operation
    ref_359370 = (0xF & ref_359362) # AND operation
    ref_360370 = ref_359370 # MOV operation
    ref_360378 = (0x1 | ref_360370) # OR operation
    ref_361357 = ref_360378 # MOV operation
    ref_361359 = ((0x40 - ref_361357) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_361367 = ref_361359 # MOV operation
    ref_361852 = ref_353287 # MOV operation
    ref_361858 = ref_361367 # MOV operation
    ref_361860 = (ref_361858 & 0xFFFFFFFF) # MOV operation
    ref_361862 = (ref_361852 >> ((ref_361860 & 0xFF) & 0x3F)) # SHR operation
    ref_361869 = ref_361862 # MOV operation
    ref_362420 = ref_349078 # MOV operation
    ref_362426 = ref_361869 # MOV operation
    ref_362428 = (ref_362426 | ref_362420) # OR operation
    ref_363479 = ref_362428 # MOV operation
    ref_363487 = (0x7 & ref_363479) # AND operation
    ref_364035 = ref_363487 # MOV operation
    ref_364053 = ((ref_364035 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_364060 = ref_364053 # MOV operation
    ref_364507 = ref_336747 # MOV operation
    ref_364513 = ref_364060 # MOV operation
    ref_364515 = (ref_364513 | ref_364507) # OR operation
    ref_368661 = ref_364515 # MOV operation
    ref_368663 = ((ref_368661 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_368664 = ((ref_368661 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_368665 = ((ref_368661 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_368666 = ((ref_368661 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_368667 = ((ref_368661 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_368668 = ((ref_368661 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_368669 = ((ref_368661 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_368670 = (ref_368661 & 0xFF) # Byte reference - MOV operation
    ref_424399 = ref_301514 # MOV operation
    ref_425433 = ref_424399 # MOV operation
    ref_425443 = (ref_425433 >> (0x3 & 0x3F)) # SHR operation
    ref_425450 = ref_425443 # MOV operation
    ref_426471 = ref_425450 # MOV operation
    ref_426479 = (0xF & ref_426471) # AND operation
    ref_427450 = ref_426479 # MOV operation
    ref_427458 = (0x1 | ref_427450) # OR operation
    ref_431627 = ref_301514 # MOV operation
    ref_432100 = ref_431627 # MOV operation
    ref_432114 = ref_427458 # MOV operation
    ref_432116 = (ref_432114 & 0xFFFFFFFF) # MOV operation
    ref_432118 = ((ref_432100 << ((ref_432116 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_432125 = ref_432118 # MOV operation
    ref_436257 = ref_301514 # MOV operation
    ref_440301 = ref_301514 # MOV operation
    ref_441300 = ref_440301 # MOV operation
    ref_441310 = (ref_441300 >> (0x3 & 0x3F)) # SHR operation
    ref_441317 = ref_441310 # MOV operation
    ref_442369 = ref_441317 # MOV operation
    ref_442377 = (0xF & ref_442369) # AND operation
    ref_443386 = ref_442377 # MOV operation
    ref_443394 = (0x1 | ref_443386) # OR operation
    ref_444401 = ref_443394 # MOV operation
    ref_444403 = ((0x40 - ref_444401) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_444411 = ref_444403 # MOV operation
    ref_444942 = ref_436257 # MOV operation
    ref_444948 = ref_444411 # MOV operation
    ref_444950 = (ref_444948 & 0xFFFFFFFF) # MOV operation
    ref_444952 = (ref_444942 >> ((ref_444950 & 0xFF) & 0x3F)) # SHR operation
    ref_444959 = ref_444952 # MOV operation
    ref_445420 = ref_432125 # MOV operation
    ref_445426 = ref_444959 # MOV operation
    ref_445428 = (ref_445426 | ref_445420) # OR operation
    ref_449579 = ref_445428 # MOV operation
    ref_456653 = ref_368669 # MOVZX operation
    ref_457647 = (ref_456653 & 0xFF) # MOVZX operation
    ref_464714 = ref_368667 # MOVZX operation
    ref_471790 = (ref_464714 & 0xFF) # MOVZX operation
    ref_471792 = (ref_471790 & 0xFF) # Byte reference - MOV operation
    ref_472852 = (ref_457647 & 0xFF) # MOVZX operation
    ref_479897 = (ref_472852 & 0xFF) # MOVZX operation
    ref_479899 = (ref_479897 & 0xFF) # Byte reference - MOV operation
    ref_484521 = ref_301514 # MOV operation
    ref_488641 = ((((((((ref_368663) << 8 | ref_368664) << 8 | ref_368665) << 8 | ref_368666) << 8 | ref_479899) << 8 | ref_368668) << 8 | ref_471792) << 8 | ref_368670) # MOV operation
    ref_489106 = ref_488641 # MOV operation
    ref_489120 = ref_484521 # MOV operation
    ref_489122 = (((sx(0x40, ref_489120) * sx(0x40, ref_489106)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_493186 = ref_449579 # MOV operation
    ref_497265 = ref_274320 # MOV operation
    ref_497798 = ref_493186 # MOV operation
    ref_497804 = ref_497265 # MOV operation
    ref_497806 = (ref_497804 | ref_497798) # OR operation
    ref_498254 = ref_497806 # MOV operation
    ref_498268 = ref_489122 # MOV operation
    ref_498270 = (((sx(0x40, ref_498268) * sx(0x40, ref_498254)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_502388 = ref_498270 # MOV operation
    ref_503374 = ref_502388 # MOV operation
    ref_503376 = ref_503374 # MOV operation
    endb = ref_503376


print endb & 0xffffffffffffffff