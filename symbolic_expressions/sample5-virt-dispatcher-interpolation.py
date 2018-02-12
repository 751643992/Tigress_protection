#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_273 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_274 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_275 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_276 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_277 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_278 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_279 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_280 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_35039 = ref_280 # MOVZX operation
ref_35628 = (ref_35039 & 0xFF) # MOVZX operation
ref_35630 = (ref_35628 & 0xFF) # MOVZX operation
ref_36237 = (ref_35630 & 0xFFFFFFFF) # MOV operation
ref_36239 = (((ref_36237 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_36613 = (ref_36239 & 0xFFFFFFFF) # MOV operation
ref_38530 = (ref_36613 & 0xFFFFFFFF) # MOV operation
ref_39776 = (ref_36613 & 0xFFFFFFFF) # MOV operation
ref_41269 = (ref_39776 & 0xFFFFFFFF) # MOV operation
ref_41277 = (((ref_41269 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_41284 = (ref_41277 & 0xFFFFFFFF) # MOV operation
ref_41907 = (ref_38530 & 0xFFFFFFFF) # MOV operation
ref_41911 = (ref_41284 & 0xFFFFFFFF) # MOV operation
ref_41913 = (((ref_41911 & 0xFFFFFFFF) + (ref_41907 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_42287 = (ref_41913 & 0xFFFFFFFF) # MOV operation
ref_44204 = (ref_42287 & 0xFFFFFFFF) # MOV operation
ref_45442 = (ref_44204 & 0xFFFFFFFF) # MOV operation
ref_45450 = ((ref_45442 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_45457 = (ref_45450 & 0xFFFFFFFF) # MOV operation
ref_46723 = (ref_42287 & 0xFFFFFFFF) # MOV operation
ref_47318 = (ref_46723 & 0xFFFFFFFF) # MOV operation
ref_47330 = (ref_45457 & 0xFFFFFFFF) # MOV operation
ref_47332 = ((ref_47330 & 0xFFFFFFFF) ^ (ref_47318 & 0xFFFFFFFF)) # XOR operation
ref_47705 = (ref_47332 & 0xFFFFFFFF) # MOV operation
ref_61210 = (ref_47705 & 0xFFFFFFFF) # MOV operation
ref_67032 = ref_279 # MOVZX operation
ref_67621 = (ref_67032 & 0xFF) # MOVZX operation
ref_67623 = (ref_67621 & 0xFF) # MOVZX operation
ref_68226 = (ref_61210 & 0xFFFFFFFF) # MOV operation
ref_68230 = (ref_67623 & 0xFFFFFFFF) # MOV operation
ref_68232 = (((ref_68230 & 0xFFFFFFFF) + (ref_68226 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_68606 = (ref_68232 & 0xFFFFFFFF) # MOV operation
ref_70523 = (ref_68606 & 0xFFFFFFFF) # MOV operation
ref_71769 = (ref_68606 & 0xFFFFFFFF) # MOV operation
ref_73262 = (ref_71769 & 0xFFFFFFFF) # MOV operation
ref_73270 = (((ref_73262 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_73277 = (ref_73270 & 0xFFFFFFFF) # MOV operation
ref_73900 = (ref_70523 & 0xFFFFFFFF) # MOV operation
ref_73904 = (ref_73277 & 0xFFFFFFFF) # MOV operation
ref_73906 = (((ref_73904 & 0xFFFFFFFF) + (ref_73900 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_74280 = (ref_73906 & 0xFFFFFFFF) # MOV operation
ref_76197 = (ref_74280 & 0xFFFFFFFF) # MOV operation
ref_77435 = (ref_76197 & 0xFFFFFFFF) # MOV operation
ref_77443 = ((ref_77435 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_77450 = (ref_77443 & 0xFFFFFFFF) # MOV operation
ref_78716 = (ref_74280 & 0xFFFFFFFF) # MOV operation
ref_79311 = (ref_78716 & 0xFFFFFFFF) # MOV operation
ref_79323 = (ref_77450 & 0xFFFFFFFF) # MOV operation
ref_79325 = ((ref_79323 & 0xFFFFFFFF) ^ (ref_79311 & 0xFFFFFFFF)) # XOR operation
ref_79698 = (ref_79325 & 0xFFFFFFFF) # MOV operation
ref_93203 = (ref_79698 & 0xFFFFFFFF) # MOV operation
ref_99025 = ref_278 # MOVZX operation
ref_99614 = (ref_99025 & 0xFF) # MOVZX operation
ref_99616 = (ref_99614 & 0xFF) # MOVZX operation
ref_100219 = (ref_93203 & 0xFFFFFFFF) # MOV operation
ref_100223 = (ref_99616 & 0xFFFFFFFF) # MOV operation
ref_100225 = (((ref_100223 & 0xFFFFFFFF) + (ref_100219 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_100599 = (ref_100225 & 0xFFFFFFFF) # MOV operation
ref_102516 = (ref_100599 & 0xFFFFFFFF) # MOV operation
ref_103762 = (ref_100599 & 0xFFFFFFFF) # MOV operation
ref_105255 = (ref_103762 & 0xFFFFFFFF) # MOV operation
ref_105263 = (((ref_105255 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_105270 = (ref_105263 & 0xFFFFFFFF) # MOV operation
ref_105893 = (ref_102516 & 0xFFFFFFFF) # MOV operation
ref_105897 = (ref_105270 & 0xFFFFFFFF) # MOV operation
ref_105899 = (((ref_105897 & 0xFFFFFFFF) + (ref_105893 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_106273 = (ref_105899 & 0xFFFFFFFF) # MOV operation
ref_108190 = (ref_106273 & 0xFFFFFFFF) # MOV operation
ref_109428 = (ref_108190 & 0xFFFFFFFF) # MOV operation
ref_109436 = ((ref_109428 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_109443 = (ref_109436 & 0xFFFFFFFF) # MOV operation
ref_110709 = (ref_106273 & 0xFFFFFFFF) # MOV operation
ref_111304 = (ref_110709 & 0xFFFFFFFF) # MOV operation
ref_111316 = (ref_109443 & 0xFFFFFFFF) # MOV operation
ref_111318 = ((ref_111316 & 0xFFFFFFFF) ^ (ref_111304 & 0xFFFFFFFF)) # XOR operation
ref_111691 = (ref_111318 & 0xFFFFFFFF) # MOV operation
ref_125196 = (ref_111691 & 0xFFFFFFFF) # MOV operation
ref_131018 = ref_277 # MOVZX operation
ref_131607 = (ref_131018 & 0xFF) # MOVZX operation
ref_131609 = (ref_131607 & 0xFF) # MOVZX operation
ref_132212 = (ref_125196 & 0xFFFFFFFF) # MOV operation
ref_132216 = (ref_131609 & 0xFFFFFFFF) # MOV operation
ref_132218 = (((ref_132216 & 0xFFFFFFFF) + (ref_132212 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_132592 = (ref_132218 & 0xFFFFFFFF) # MOV operation
ref_134509 = (ref_132592 & 0xFFFFFFFF) # MOV operation
ref_135755 = (ref_132592 & 0xFFFFFFFF) # MOV operation
ref_137248 = (ref_135755 & 0xFFFFFFFF) # MOV operation
ref_137256 = (((ref_137248 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_137263 = (ref_137256 & 0xFFFFFFFF) # MOV operation
ref_137886 = (ref_134509 & 0xFFFFFFFF) # MOV operation
ref_137890 = (ref_137263 & 0xFFFFFFFF) # MOV operation
ref_137892 = (((ref_137890 & 0xFFFFFFFF) + (ref_137886 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_138266 = (ref_137892 & 0xFFFFFFFF) # MOV operation
ref_140183 = (ref_138266 & 0xFFFFFFFF) # MOV operation
ref_141421 = (ref_140183 & 0xFFFFFFFF) # MOV operation
ref_141429 = ((ref_141421 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_141436 = (ref_141429 & 0xFFFFFFFF) # MOV operation
ref_142702 = (ref_138266 & 0xFFFFFFFF) # MOV operation
ref_143297 = (ref_142702 & 0xFFFFFFFF) # MOV operation
ref_143309 = (ref_141436 & 0xFFFFFFFF) # MOV operation
ref_143311 = ((ref_143309 & 0xFFFFFFFF) ^ (ref_143297 & 0xFFFFFFFF)) # XOR operation
ref_143684 = (ref_143311 & 0xFFFFFFFF) # MOV operation
ref_157189 = (ref_143684 & 0xFFFFFFFF) # MOV operation
ref_163011 = ref_276 # MOVZX operation
ref_163600 = (ref_163011 & 0xFF) # MOVZX operation
ref_163602 = (ref_163600 & 0xFF) # MOVZX operation
ref_164205 = (ref_157189 & 0xFFFFFFFF) # MOV operation
ref_164209 = (ref_163602 & 0xFFFFFFFF) # MOV operation
ref_164211 = (((ref_164209 & 0xFFFFFFFF) + (ref_164205 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_164585 = (ref_164211 & 0xFFFFFFFF) # MOV operation
ref_166502 = (ref_164585 & 0xFFFFFFFF) # MOV operation
ref_167748 = (ref_164585 & 0xFFFFFFFF) # MOV operation
ref_169241 = (ref_167748 & 0xFFFFFFFF) # MOV operation
ref_169249 = (((ref_169241 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_169256 = (ref_169249 & 0xFFFFFFFF) # MOV operation
ref_169879 = (ref_166502 & 0xFFFFFFFF) # MOV operation
ref_169883 = (ref_169256 & 0xFFFFFFFF) # MOV operation
ref_169885 = (((ref_169883 & 0xFFFFFFFF) + (ref_169879 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_170259 = (ref_169885 & 0xFFFFFFFF) # MOV operation
ref_172176 = (ref_170259 & 0xFFFFFFFF) # MOV operation
ref_173414 = (ref_172176 & 0xFFFFFFFF) # MOV operation
ref_173422 = ((ref_173414 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_173429 = (ref_173422 & 0xFFFFFFFF) # MOV operation
ref_174695 = (ref_170259 & 0xFFFFFFFF) # MOV operation
ref_175290 = (ref_174695 & 0xFFFFFFFF) # MOV operation
ref_175302 = (ref_173429 & 0xFFFFFFFF) # MOV operation
ref_175304 = ((ref_175302 & 0xFFFFFFFF) ^ (ref_175290 & 0xFFFFFFFF)) # XOR operation
ref_175677 = (ref_175304 & 0xFFFFFFFF) # MOV operation
ref_189182 = (ref_175677 & 0xFFFFFFFF) # MOV operation
ref_195004 = ref_275 # MOVZX operation
ref_195593 = (ref_195004 & 0xFF) # MOVZX operation
ref_195595 = (ref_195593 & 0xFF) # MOVZX operation
ref_196198 = (ref_189182 & 0xFFFFFFFF) # MOV operation
ref_196202 = (ref_195595 & 0xFFFFFFFF) # MOV operation
ref_196204 = (((ref_196202 & 0xFFFFFFFF) + (ref_196198 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_196578 = (ref_196204 & 0xFFFFFFFF) # MOV operation
ref_198495 = (ref_196578 & 0xFFFFFFFF) # MOV operation
ref_199741 = (ref_196578 & 0xFFFFFFFF) # MOV operation
ref_201234 = (ref_199741 & 0xFFFFFFFF) # MOV operation
ref_201242 = (((ref_201234 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_201249 = (ref_201242 & 0xFFFFFFFF) # MOV operation
ref_201872 = (ref_198495 & 0xFFFFFFFF) # MOV operation
ref_201876 = (ref_201249 & 0xFFFFFFFF) # MOV operation
ref_201878 = (((ref_201876 & 0xFFFFFFFF) + (ref_201872 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_202252 = (ref_201878 & 0xFFFFFFFF) # MOV operation
ref_204169 = (ref_202252 & 0xFFFFFFFF) # MOV operation
ref_205407 = (ref_204169 & 0xFFFFFFFF) # MOV operation
ref_205415 = ((ref_205407 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_205422 = (ref_205415 & 0xFFFFFFFF) # MOV operation
ref_206688 = (ref_202252 & 0xFFFFFFFF) # MOV operation
ref_207283 = (ref_206688 & 0xFFFFFFFF) # MOV operation
ref_207295 = (ref_205422 & 0xFFFFFFFF) # MOV operation
ref_207297 = ((ref_207295 & 0xFFFFFFFF) ^ (ref_207283 & 0xFFFFFFFF)) # XOR operation
ref_207670 = (ref_207297 & 0xFFFFFFFF) # MOV operation
ref_221175 = (ref_207670 & 0xFFFFFFFF) # MOV operation
ref_226997 = ref_274 # MOVZX operation
ref_227586 = (ref_226997 & 0xFF) # MOVZX operation
ref_227588 = (ref_227586 & 0xFF) # MOVZX operation
ref_228191 = (ref_221175 & 0xFFFFFFFF) # MOV operation
ref_228195 = (ref_227588 & 0xFFFFFFFF) # MOV operation
ref_228197 = (((ref_228195 & 0xFFFFFFFF) + (ref_228191 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_228571 = (ref_228197 & 0xFFFFFFFF) # MOV operation
ref_230488 = (ref_228571 & 0xFFFFFFFF) # MOV operation
ref_231734 = (ref_228571 & 0xFFFFFFFF) # MOV operation
ref_233227 = (ref_231734 & 0xFFFFFFFF) # MOV operation
ref_233235 = (((ref_233227 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_233242 = (ref_233235 & 0xFFFFFFFF) # MOV operation
ref_233865 = (ref_230488 & 0xFFFFFFFF) # MOV operation
ref_233869 = (ref_233242 & 0xFFFFFFFF) # MOV operation
ref_233871 = (((ref_233869 & 0xFFFFFFFF) + (ref_233865 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_234245 = (ref_233871 & 0xFFFFFFFF) # MOV operation
ref_236162 = (ref_234245 & 0xFFFFFFFF) # MOV operation
ref_237400 = (ref_236162 & 0xFFFFFFFF) # MOV operation
ref_237408 = ((ref_237400 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_237415 = (ref_237408 & 0xFFFFFFFF) # MOV operation
ref_238681 = (ref_234245 & 0xFFFFFFFF) # MOV operation
ref_239276 = (ref_238681 & 0xFFFFFFFF) # MOV operation
ref_239288 = (ref_237415 & 0xFFFFFFFF) # MOV operation
ref_239290 = ((ref_239288 & 0xFFFFFFFF) ^ (ref_239276 & 0xFFFFFFFF)) # XOR operation
ref_239663 = (ref_239290 & 0xFFFFFFFF) # MOV operation
ref_253168 = (ref_239663 & 0xFFFFFFFF) # MOV operation
ref_258990 = ref_273 # MOVZX operation
ref_259579 = (ref_258990 & 0xFF) # MOVZX operation
ref_259581 = (ref_259579 & 0xFF) # MOVZX operation
ref_260184 = (ref_253168 & 0xFFFFFFFF) # MOV operation
ref_260188 = (ref_259581 & 0xFFFFFFFF) # MOV operation
ref_260190 = (((ref_260188 & 0xFFFFFFFF) + (ref_260184 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_260564 = (ref_260190 & 0xFFFFFFFF) # MOV operation
ref_262481 = (ref_260564 & 0xFFFFFFFF) # MOV operation
ref_263727 = (ref_260564 & 0xFFFFFFFF) # MOV operation
ref_265220 = (ref_263727 & 0xFFFFFFFF) # MOV operation
ref_265228 = (((ref_265220 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_265235 = (ref_265228 & 0xFFFFFFFF) # MOV operation
ref_265858 = (ref_262481 & 0xFFFFFFFF) # MOV operation
ref_265862 = (ref_265235 & 0xFFFFFFFF) # MOV operation
ref_265864 = (((ref_265862 & 0xFFFFFFFF) + (ref_265858 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_266238 = (ref_265864 & 0xFFFFFFFF) # MOV operation
ref_268155 = (ref_266238 & 0xFFFFFFFF) # MOV operation
ref_269393 = (ref_268155 & 0xFFFFFFFF) # MOV operation
ref_269401 = ((ref_269393 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_269408 = (ref_269401 & 0xFFFFFFFF) # MOV operation
ref_270674 = (ref_266238 & 0xFFFFFFFF) # MOV operation
ref_271269 = (ref_270674 & 0xFFFFFFFF) # MOV operation
ref_271281 = (ref_269408 & 0xFFFFFFFF) # MOV operation
ref_271283 = ((ref_271281 & 0xFFFFFFFF) ^ (ref_271269 & 0xFFFFFFFF)) # XOR operation
ref_271656 = (ref_271283 & 0xFFFFFFFF) # MOV operation
ref_279090 = (ref_271656 & 0xFFFFFFFF) # MOV operation
ref_280336 = (ref_271656 & 0xFFFFFFFF) # MOV operation
ref_281829 = (ref_280336 & 0xFFFFFFFF) # MOV operation
ref_281837 = (((ref_281829 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_281844 = (ref_281837 & 0xFFFFFFFF) # MOV operation
ref_282467 = (ref_279090 & 0xFFFFFFFF) # MOV operation
ref_282471 = (ref_281844 & 0xFFFFFFFF) # MOV operation
ref_282473 = (((ref_282471 & 0xFFFFFFFF) + (ref_282467 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_282847 = (ref_282473 & 0xFFFFFFFF) # MOV operation
ref_284764 = (ref_282847 & 0xFFFFFFFF) # MOV operation
ref_286002 = (ref_284764 & 0xFFFFFFFF) # MOV operation
ref_286010 = ((ref_286002 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_286017 = (ref_286010 & 0xFFFFFFFF) # MOV operation
ref_287283 = (ref_282847 & 0xFFFFFFFF) # MOV operation
ref_287878 = (ref_287283 & 0xFFFFFFFF) # MOV operation
ref_287890 = (ref_286017 & 0xFFFFFFFF) # MOV operation
ref_287892 = ((ref_287890 & 0xFFFFFFFF) ^ (ref_287878 & 0xFFFFFFFF)) # XOR operation
ref_288265 = (ref_287892 & 0xFFFFFFFF) # MOV operation
ref_290182 = (ref_288265 & 0xFFFFFFFF) # MOV operation
ref_291428 = (ref_288265 & 0xFFFFFFFF) # MOV operation
ref_292921 = (ref_291428 & 0xFFFFFFFF) # MOV operation
ref_292929 = (((ref_292921 & 0xFFFFFFFF) << (0xF & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_292936 = (ref_292929 & 0xFFFFFFFF) # MOV operation
ref_293559 = (ref_290182 & 0xFFFFFFFF) # MOV operation
ref_293563 = (ref_292936 & 0xFFFFFFFF) # MOV operation
ref_293565 = (((ref_293563 & 0xFFFFFFFF) + (ref_293559 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_293939 = (ref_293565 & 0xFFFFFFFF) # MOV operation
ref_295812 = (ref_293939 & 0xFFFFFFFF) # MOV operation
ref_296148 = (ref_295812 & 0xFFFFFFFF) # MOV operation
ref_296172 = (ref_296148 & 0xFFFFFFFF) # MOV operation
ref_296180 = (ref_296172 & 0xFFFFFFFF) # MOV operation
ref_296182 = (ref_296180 & 0xFFFFFFFF) # MOV operation

print ref_296182 & 0xffffffffffffffff