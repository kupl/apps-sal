""""
YOU ARE LOOKING AT THE MIGHTIEST OF CODE!!!!!

HERE IS THE INEFFICIENT PROGRAM THAT WROTE MY FUNCTION:

def operator_insertor(n):
    bestsofar = 10
    for i in range(3**8):
        if eval(genstr(i)) == n:
            a=list(tc(i))
            while a.count(" "):
                a.remove(" ")
            if len(a) < bestsofar:
                bestsofar = len(a)
    if bestsofar == 10:
        return None
    else:
        return bestsofar
    # your code here
def genstr(y):
    a=list("123456789")
    b=list(tc(y))
    c = [item for pair in zip(a, b) for item in pair]
    while (c.count(" ")):
        c.remove(" ")
    d = ''.join(c)
    return d

def tc(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    while len(nums) < 8:
        nums.append("0")
    streng = ''.join(reversed(nums))
    intab="012"
    outtab=" +-"
    trantab = str.maketrans(intab, outtab)
    return streng.translate(trantab)+" "
print("def operator_insertor(n):")
for i in range(1001):
    print("    if n ==",i,":")
    print("        return",operator_insertor(i))
    
-------------

I realise that with my code I could have written a more efficient final function, but it's for the laughs gentlemen

THANK YOU AND HAVE A NICE DAY :)
"""

def operator_insertor(n):
    if n == 0 :
        return 5
    if n == 1 :
        return 4
    if n == 2 :
        return 4
    if n == 3 :
        return 4
    if n == 4 :
        return 4
    if n == 5 :
        return 4
    if n == 6 :
        return 4
    if n == 7 :
        return 5
    if n == 8 :
        return 5
    if n == 9 :
        return 4
    if n == 10 :
        return 1
    if n == 11 :
        return 5
    if n == 12 :
        return 3
    if n == 13 :
        return 5
    if n == 14 :
        return 5
    if n == 15 :
        return 4
    if n == 16 :
        return 5
    if n == 17 :
        return 5
    if n == 18 :
        return 4
    if n == 19 :
        return 4
    if n == 20 :
        return 4
    if n == 21 :
        return 5
    if n == 22 :
        return 5
    if n == 23 :
        return 5
    if n == 24 :
        return 5
    if n == 25 :
        return 5
    if n == 26 :
        return 5
    if n == 27 :
        return 5
    if n == 28 :
        return 4
    if n == 29 :
        return 4
    if n == 30 :
        return 5
    if n == 31 :
        return 5
    if n == 32 :
        return 4
    if n == 33 :
        return 4
    if n == 34 :
        return 5
    if n == 35 :
        return 5
    if n == 36 :
        return 5
    if n == 37 :
        return 5
    if n == 38 :
        return 4
    if n == 39 :
        return 5
    if n == 40 :
        return 5
    if n == 41 :
        return 5
    if n == 42 :
        return 5
    if n == 43 :
        return 5
    if n == 44 :
        return 5
    if n == 45 :
        return 4
    if n == 46 :
        return 5
    if n == 47 :
        return 4
    if n == 48 :
        return 5
    if n == 49 :
        return 5
    if n == 50 :
        return 5
    if n == 51 :
        return 5
    if n == 52 :
        return 5
    if n == 53 :
        return 5
    if n == 54 :
        return 5
    if n == 55 :
        return 5
    if n == 56 :
        return 3
    if n == 57 :
        return 5
    if n == 58 :
        return 5
    if n == 59 :
        return 4
    if n == 60 :
        return 5
    if n == 61 :
        return 5
    if n == 62 :
        return 5
    if n == 63 :
        return 4
    if n == 64 :
        return 5
    if n == 65 :
        return 5
    if n == 66 :
        return 4
    if n == 67 :
        return 5
    if n == 68 :
        return 5
    if n == 69 :
        return 5
    if n == 70 :
        return 6
    if n == 71 :
        return 5
    if n == 72 :
        return 4
    if n == 73 :
        return 4
    if n == 74 :
        return 4
    if n == 75 :
        return 4
    if n == 76 :
        return 4
    if n == 77 :
        return 4
    if n == 78 :
        return 4
    if n == 79 :
        return 4
    if n == 80 :
        return 4
    if n == 81 :
        return 5
    if n == 82 :
        return 4
    if n == 83 :
        return 4
    if n == 84 :
        return 4
    if n == 85 :
        return 5
    if n == 86 :
        return 4
    if n == 87 :
        return 4
    if n == 88 :
        return 4
    if n == 89 :
        return 4
    if n == 90 :
        return 5
    if n == 91 :
        return 4
    if n == 92 :
        return 4
    if n == 93 :
        return 4
    if n == 94 :
        return 5
    if n == 95 :
        return 5
    if n == 96 :
        return 4
    if n == 97 :
        return 4
    if n == 98 :
        return 5
    if n == 99 :
        return 5
    if n == 100 :
        return 3
    if n == 101 :
        return 4
    if n == 102 :
        return 4
    if n == 103 :
        return 4
    if n == 104 :
        return 5
    if n == 105 :
        return 4
    if n == 106 :
        return 4
    if n == 107 :
        return 5
    if n == 108 :
        return 5
    if n == 109 :
        return 5
    if n == 110 :
        return 4
    if n == 111 :
        return 5
    if n == 112 :
        return 5
    if n == 113 :
        return 5
    if n == 114 :
        return 4
    if n == 115 :
        return 6
    if n == 116 :
        return 4
    if n == 117 :
        return 5
    if n == 118 :
        return 4
    if n == 119 :
        return 5
    if n == 120 :
        return 4
    if n == 121 :
        return 4
    if n == 122 :
        return 5
    if n == 123 :
        return 5
    if n == 124 :
        return 6
    if n == 125 :
        return 5
    if n == 126 :
        return 4
    if n == 127 :
        return 5
    if n == 128 :
        return 4
    if n == 129 :
        return 4
    if n == 130 :
        return 4
    if n == 131 :
        return 5
    if n == 132 :
        return 4
    if n == 133 :
        return 5
    if n == 134 :
        return 5
    if n == 135 :
        return 4
    if n == 136 :
        return 4
    if n == 137 :
        return 5
    if n == 138 :
        return 5
    if n == 139 :
        return 4
    if n == 140 :
        return 4
    if n == 141 :
        return 4
    if n == 142 :
        return 5
    if n == 143 :
        return 5
    if n == 144 :
        return 4
    if n == 145 :
        return 4
    if n == 146 :
        return 3
    if n == 147 :
        return 5
    if n == 148 :
        return 5
    if n == 149 :
        return 5
    if n == 150 :
        return 4
    if n == 151 :
        return 5
    if n == 152 :
        return 5
    if n == 153 :
        return 4
    if n == 154 :
        return 4
    if n == 155 :
        return 5
    if n == 156 :
        return 5
    if n == 157 :
        return 5
    if n == 158 :
        return 4
    if n == 159 :
        return 4
    if n == 160 :
        return None
    if n == 161 :
        return 6
    if n == 162 :
        return 4
    if n == 163 :
        return 5
    if n == 164 :
        return 5
    if n == 165 :
        return 5
    if n == 166 :
        return 4
    if n == 167 :
        return 4
    if n == 168 :
        return 4
    if n == 169 :
        return 5
    if n == 170 :
        return 5
    if n == 171 :
        return 4
    if n == 172 :
        return 5
    if n == 173 :
        return 5
    if n == 174 :
        return 5
    if n == 175 :
        return 5
    if n == 176 :
        return 5
    if n == 177 :
        return 5
    if n == 178 :
        return None
    if n == 179 :
        return 4
    if n == 180 :
        return 4
    if n == 181 :
        return 5
    if n == 182 :
        return 5
    if n == 183 :
        return 5
    if n == 184 :
        return 4
    if n == 185 :
        return 5
    if n == 186 :
        return 5
    if n == 187 :
        return 5
    if n == 188 :
        return 4
    if n == 189 :
        return 4
    if n == 190 :
        return 3
    if n == 191 :
        return 5
    if n == 192 :
        return 4
    if n == 193 :
        return 5
    if n == 194 :
        return 5
    if n == 195 :
        return 4
    if n == 196 :
        return None
    if n == 197 :
        return 4
    if n == 198 :
        return 4
    if n == 199 :
        return 5
    if n == 200 :
        return 5
    if n == 201 :
        return 3
    if n == 202 :
        return 5
    if n == 203 :
        return 5
    if n == 204 :
        return 4
    if n == 205 :
        return 5
    if n == 206 :
        return 5
    if n == 207 :
        return 4
    if n == 208 :
        return 4
    if n == 209 :
        return 4
    if n == 210 :
        return 4
    if n == 211 :
        return None
    if n == 212 :
        return 5
    if n == 213 :
        return 5
    if n == 214 :
        return 5
    if n == 215 :
        return 5
    if n == 216 :
        return 4
    if n == 217 :
        return 5
    if n == 218 :
        return 4
    if n == 219 :
        return None
    if n == 220 :
        return 5
    if n == 221 :
        return None
    if n == 222 :
        return 4
    if n == 223 :
        return None
    if n == 224 :
        return 5
    if n == 225 :
        return 4
    if n == 226 :
        return 5
    if n == 227 :
        return None
    if n == 228 :
        return 6
    if n == 229 :
        return None
    if n == 230 :
        return 6
    if n == 231 :
        return 4
    if n == 232 :
        return 6
    if n == 233 :
        return None
    if n == 234 :
        return 3
    if n == 235 :
        return None
    if n == 236 :
        return 4
    if n == 237 :
        return None
    if n == 238 :
        return 6
    if n == 239 :
        return None
    if n == 240 :
        return 6
    if n == 241 :
        return None
    if n == 242 :
        return 5
    if n == 243 :
        return 4
    if n == 244 :
        return 4
    if n == 245 :
        return 3
    if n == 246 :
        return 5
    if n == 247 :
        return None
    if n == 248 :
        return 4
    if n == 249 :
        return 4
    if n == 250 :
        return None
    if n == 251 :
        return 5
    if n == 252 :
        return 4
    if n == 253 :
        return None
    if n == 254 :
        return 5
    if n == 255 :
        return 4
    if n == 256 :
        return 4
    if n == 257 :
        return 4
    if n == 258 :
        return 4
    if n == 259 :
        return None
    if n == 260 :
        return 5
    if n == 261 :
        return 4
    if n == 262 :
        return 4
    if n == 263 :
        return 5
    if n == 264 :
        return 4
    if n == 265 :
        return 4
    if n == 266 :
        return 4
    if n == 267 :
        return 4
    if n == 268 :
        return 5
    if n == 269 :
        return 4
    if n == 270 :
        return 4
    if n == 271 :
        return 4
    if n == 272 :
        return 5
    if n == 273 :
        return 4
    if n == 274 :
        return None
    if n == 275 :
        return 4
    if n == 276 :
        return 4
    if n == 277 :
        return None
    if n == 278 :
        return 4
    if n == 279 :
        return 4
    if n == 280 :
        return 4
    if n == 281 :
        return 4
    if n == 282 :
        return 4
    if n == 283 :
        return 5
    if n == 284 :
        return None
    if n == 285 :
        return 5
    if n == 286 :
        return None
    if n == 287 :
        return None
    if n == 288 :
        return 4
    if n == 289 :
        return 4
    if n == 290 :
        return 5
    if n == 291 :
        return 4
    if n == 292 :
        return None
    if n == 293 :
        return 5
    if n == 294 :
        return 4
    if n == 295 :
        return None
    if n == 296 :
        return 5
    if n == 297 :
        return 5
    if n == 298 :
        return 5
    if n == 299 :
        return 5
    if n == 300 :
        return None
    if n == 301 :
        return 5
    if n == 302 :
        return None
    if n == 303 :
        return 5
    if n == 304 :
        return None
    if n == 305 :
        return 5
    if n == 306 :
        return 5
    if n == 307 :
        return 4
    if n == 308 :
        return 5
    if n == 309 :
        return None
    if n == 310 :
        return None
    if n == 311 :
        return 3
    if n == 312 :
        return None
    if n == 313 :
        return None
    if n == 314 :
        return 5
    if n == 315 :
        return 5
    if n == 316 :
        return 5
    if n == 317 :
        return 4
    if n == 318 :
        return 5
    if n == 319 :
        return None
    if n == 320 :
        return 5
    if n == 321 :
        return 5
    if n == 322 :
        return 4
    if n == 323 :
        return 4
    if n == 324 :
        return 3
    if n == 325 :
        return None
    if n == 326 :
        return 4
    if n == 327 :
        return 4
    if n == 328 :
        return 5
    if n == 329 :
        return 4
    if n == 330 :
        return 5
    if n == 331 :
        return None
    if n == 332 :
        return 5
    if n == 333 :
        return 4
    if n == 334 :
        return 6
    if n == 335 :
        return 3
    if n == 336 :
        return 3
    if n == 337 :
        return None
    if n == 338 :
        return 4
    if n == 339 :
        return 4
    if n == 340 :
        return 6
    if n == 341 :
        return 4
    if n == 342 :
        return 3
    if n == 343 :
        return 5
    if n == 344 :
        return 6
    if n == 345 :
        return 4
    if n == 346 :
        return 6
    if n == 347 :
        return 4
    if n == 348 :
        return 3
    if n == 349 :
        return None
    if n == 350 :
        return 6
    if n == 351 :
        return 4
    if n == 352 :
        return 4
    if n == 353 :
        return 5
    if n == 354 :
        return 3
    if n == 355 :
        return 5
    if n == 356 :
        return 5
    if n == 357 :
        return 3
    if n == 358 :
        return 6
    if n == 359 :
        return 5
    if n == 360 :
        return 4
    if n == 361 :
        return 5
    if n == 362 :
        return 5
    if n == 363 :
        return None
    if n == 364 :
        return 6
    if n == 365 :
        return 4
    if n == 366 :
        return 4
    if n == 367 :
        return None
    if n == 368 :
        return None
    if n == 369 :
        return 4
    if n == 370 :
        return 4
    if n == 371 :
        return 5
    if n == 372 :
        return None
    if n == 373 :
        return 4
    if n == 374 :
        return 5
    if n == 375 :
        return 4
    if n == 376 :
        return 5
    if n == 377 :
        return None
    if n == 378 :
        return 4
    if n == 379 :
        return 3
    if n == 380 :
        return 5
    if n == 381 :
        return None
    if n == 382 :
        return None
    if n == 383 :
        return 4
    if n == 384 :
        return 4
    if n == 385 :
        return None
    if n == 386 :
        return 4
    if n == 387 :
        return 4
    if n == 388 :
        return None
    if n == 389 :
        return 2
    if n == 390 :
        return None
    if n == 391 :
        return None
    if n == 392 :
        return None
    if n == 393 :
        return 4
    if n == 394 :
        return 5
    if n == 395 :
        return None
    if n == 396 :
        return 4
    if n == 397 :
        return None
    if n == 398 :
        return 4
    if n == 399 :
        return None
    if n == 400 :
        return None
    if n == 401 :
        return None
    if n == 402 :
        return 4
    if n == 403 :
        return None
    if n == 404 :
        return None
    if n == 405 :
        return None
    if n == 406 :
        return None
    if n == 407 :
        return 4
    if n == 408 :
        return None
    if n == 409 :
        return None
    if n == 410 :
        return 5
    if n == 411 :
        return 4
    if n == 412 :
        return 5
    if n == 413 :
        return None
    if n == 414 :
        return 5
    if n == 415 :
        return None
    if n == 416 :
        return 5
    if n == 417 :
        return None
    if n == 418 :
        return None
    if n == 419 :
        return 5
    if n == 420 :
        return 4
    if n == 421 :
        return None
    if n == 422 :
        return None
    if n == 423 :
        return 3
    if n == 424 :
        return 5
    if n == 425 :
        return 4
    if n == 426 :
        return 5
    if n == 427 :
        return None
    if n == 428 :
        return 5
    if n == 429 :
        return 5
    if n == 430 :
        return None
    if n == 431 :
        return 4
    if n == 432 :
        return 4
    if n == 433 :
        return 4
    if n == 434 :
        return 3
    if n == 435 :
        return None
    if n == 436 :
        return 5
    if n == 437 :
        return 4
    if n == 438 :
        return 4
    if n == 439 :
        return None
    if n == 440 :
        return 5
    if n == 441 :
        return 4
    if n == 442 :
        return 5
    if n == 443 :
        return 4
    if n == 444 :
        return 3
    if n == 445 :
        return 4
    if n == 446 :
        return 3
    if n == 447 :
        return 4
    if n == 448 :
        return 6
    if n == 449 :
        return 4
    if n == 450 :
        return 3
    if n == 451 :
        return None
    if n == 452 :
        return 4
    if n == 453 :
        return 4
    if n == 454 :
        return 6
    if n == 455 :
        return 5
    if n == 456 :
        return 2
    if n == 457 :
        return 5
    if n == 458 :
        return 5
    if n == 459 :
        return 4
    if n == 460 :
        return 4
    if n == 461 :
        return 5
    if n == 462 :
        return 3
    if n == 463 :
        return 5
    if n == 464 :
        return 6
    if n == 465 :
        return 5
    if n == 466 :
        return 6
    if n == 467 :
        return None
    if n == 468 :
        return 6
    if n == 469 :
        return None
    if n == 470 :
        return 5
    if n == 471 :
        return 5
    if n == 472 :
        return 5
    if n == 473 :
        return 5
    if n == 474 :
        return 5
    if n == 475 :
        return 5
    if n == 476 :
        return 5
    if n == 477 :
        return 5
    if n == 478 :
        return 5
    if n == 479 :
        return 5
    if n == 480 :
        return 5
    if n == 481 :
        return 5
    if n == 482 :
        return 5
    if n == 483 :
        return 3
    if n == 484 :
        return 5
    if n == 485 :
        return None
    if n == 486 :
        return 5
    if n == 487 :
        return None
    if n == 488 :
        return 5
    if n == 489 :
        return 4
    if n == 490 :
        return 5
    if n == 491 :
        return 4
    if n == 492 :
        return 3
    if n == 493 :
        return None
    if n == 494 :
        return None
    if n == 495 :
        return 5
    if n == 496 :
        return None
    if n == 497 :
        return 3
    if n == 498 :
        return 4
    if n == 499 :
        return None
    if n == 500 :
        return 3
    if n == 501 :
        return 2
    if n == 502 :
        return None
    if n == 503 :
        return 4
    if n == 504 :
        return 4
    if n == 505 :
        return None
    if n == 506 :
        return 4
    if n == 507 :
        return None
    if n == 508 :
        return None
    if n == 509 :
        return None
    if n == 510 :
        return 3
    if n == 511 :
        return 4
    if n == 512 :
        return None
    if n == 513 :
        return 3
    if n == 514 :
        return None
    if n == 515 :
        return 4
    if n == 516 :
        return 4
    if n == 517 :
        return None
    if n == 518 :
        return None
    if n == 519 :
        return 5
    if n == 520 :
        return None
    if n == 521 :
        return 4
    if n == 522 :
        return None
    if n == 523 :
        return None
    if n == 524 :
        return 3
    if n == 525 :
        return 5
    if n == 526 :
        return None
    if n == 527 :
        return 5
    if n == 528 :
        return 4
    if n == 529 :
        return None
    if n == 530 :
        return 4
    if n == 531 :
        return 5
    if n == 532 :
        return 5
    if n == 533 :
        return 5
    if n == 534 :
        return 4
    if n == 535 :
        return 5
    if n == 536 :
        return None
    if n == 537 :
        return 5
    if n == 538 :
        return 5
    if n == 539 :
        return 5
    if n == 540 :
        return 4
    if n == 541 :
        return None
    if n == 542 :
        return 3
    if n == 543 :
        return 5
    if n == 544 :
        return 4
    if n == 545 :
        return 4
    if n == 546 :
        return 4
    if n == 547 :
        return 4
    if n == 548 :
        return 5
    if n == 549 :
        return 4
    if n == 550 :
        return 5
    if n == 551 :
        return None
    if n == 552 :
        return 3
    if n == 553 :
        return 4
    if n == 554 :
        return 5
    if n == 555 :
        return 4
    if n == 556 :
        return 6
    if n == 557 :
        return 4
    if n == 558 :
        return 4
    if n == 559 :
        return None
    if n == 560 :
        return 3
    if n == 561 :
        return 4
    if n == 562 :
        return 4
    if n == 563 :
        return 5
    if n == 564 :
        return 6
    if n == 565 :
        return None
    if n == 566 :
        return 5
    if n == 567 :
        return 4
    if n == 568 :
        return 6
    if n == 569 :
        return 4
    if n == 570 :
        return 3
    if n == 571 :
        return 4
    if n == 572 :
        return 6
    if n == 573 :
        return 4
    if n == 574 :
        return 6
    if n == 575 :
        return None
    if n == 576 :
        return 4
    if n == 577 :
        return 5
    if n == 578 :
        return 2
    if n == 579 :
        return 5
    if n == 580 :
        return 6
    if n == 581 :
        return 5
    if n == 582 :
        return 6
    if n == 583 :
        return 5
    if n == 584 :
        return 6
    if n == 585 :
        return 4
    if n == 586 :
        return 5
    if n == 587 :
        return 4
    if n == 588 :
        return 5
    if n == 589 :
        return 4
    if n == 590 :
        return 6
    if n == 591 :
        return None
    if n == 592 :
        return None
    if n == 593 :
        return None
    if n == 594 :
        return 5
    if n == 595 :
        return 5
    if n == 596 :
        return 4
    if n == 597 :
        return 3
    if n == 598 :
        return None
    if n == 599 :
        return 5
    if n == 600 :
        return None
    if n == 601 :
        return 5
    if n == 602 :
        return 4
    if n == 603 :
        return 4
    if n == 604 :
        return 5
    if n == 605 :
        return 3
    if n == 606 :
        return None
    if n == 607 :
        return None
    if n == 608 :
        return None
    if n == 609 :
        return None
    if n == 610 :
        return None
    if n == 611 :
        return None
    if n == 612 :
        return 3
    if n == 613 :
        return None
    if n == 614 :
        return 4
    if n == 615 :
        return None
    if n == 616 :
        return None
    if n == 617 :
        return 5
    if n == 618 :
        return None
    if n == 619 :
        return None
    if n == 620 :
        return 4
    if n == 621 :
        return 4
    if n == 622 :
        return None
    if n == 623 :
        return None
    if n == 624 :
        return 5
    if n == 625 :
        return 4
    if n == 626 :
        return 5
    if n == 627 :
        return None
    if n == 628 :
        return None
    if n == 629 :
        return 5
    if n == 630 :
        return 4
    if n == 631 :
        return None
    if n == 632 :
        return None
    if n == 633 :
        return 4
    if n == 634 :
        return 3
    if n == 635 :
        return None
    if n == 636 :
        return None
    if n == 637 :
        return None
    if n == 638 :
        return 4
    if n == 639 :
        return 4
    if n == 640 :
        return None
    if n == 641 :
        return None
    if n == 642 :
        return 4
    if n == 643 :
        return 5
    if n == 644 :
        return 5
    if n == 645 :
        return None
    if n == 646 :
        return 5
    if n == 647 :
        return 5
    if n == 648 :
        return 3
    if n == 649 :
        return None
    if n == 650 :
        return 3
    if n == 651 :
        return 4
    if n == 652 :
        return 4
    if n == 653 :
        return None
    if n == 654 :
        return 5
    if n == 655 :
        return None
    if n == 656 :
        return 5
    if n == 657 :
        return 4
    if n == 658 :
        return 5
    if n == 659 :
        return None
    if n == 660 :
        return 4
    if n == 661 :
        return 3
    if n == 662 :
        return 5
    if n == 663 :
        return None
    if n == 664 :
        return 5
    if n == 665 :
        return None
    if n == 666 :
        return 3
    if n == 667 :
        return 4
    if n == 668 :
        return 3
    if n == 669 :
        return 4
    if n == 670 :
        return 4
    if n == 671 :
        return None
    if n == 672 :
        return 6
    if n == 673 :
        return None
    if n == 674 :
        return 5
    if n == 675 :
        return 3
    if n == 676 :
        return 4
    if n == 677 :
        return 4
    if n == 678 :
        return 6
    if n == 679 :
        return 5
    if n == 680 :
        return 6
    if n == 681 :
        return None
    if n == 682 :
        return 6
    if n == 683 :
        return 5
    if n == 684 :
        return 3
    if n == 685 :
        return 4
    if n == 686 :
        return 6
    if n == 687 :
        return 4
    if n == 688 :
        return 6
    if n == 689 :
        return 4
    if n == 690 :
        return 6
    if n == 691 :
        return None
    if n == 692 :
        return 4
    if n == 693 :
        return 4
    if n == 694 :
        return 5
    if n == 695 :
        return 4
    if n == 696 :
        return 6
    if n == 697 :
        return 5
    if n == 698 :
        return 4
    if n == 699 :
        return None
    if n == 700 :
        return None
    if n == 701 :
        return 5
    if n == 702 :
        return 3
    if n == 703 :
        return 4
    if n == 704 :
        return None
    if n == 705 :
        return 5
    if n == 706 :
        return None
    if n == 707 :
        return 4
    if n == 708 :
        return None
    if n == 709 :
        return None
    if n == 710 :
        return 4
    if n == 711 :
        return 3
    if n == 712 :
        return 5
    if n == 713 :
        return 3
    if n == 714 :
        return 5
    if n == 715 :
        return 4
    if n == 716 :
        return 4
    if n == 717 :
        return None
    if n == 718 :
        return None
    if n == 719 :
        return 5
    if n == 720 :
        return 4
    if n == 721 :
        return None
    if n == 722 :
        return None
    if n == 723 :
        return 4
    if n == 724 :
        return None
    if n == 725 :
        return 5
    if n == 726 :
        return None
    if n == 727 :
        return None
    if n == 728 :
        return 4
    if n == 729 :
        return 4
    if n == 730 :
        return None
    if n == 731 :
        return 5
    if n == 732 :
        return 5
    if n == 733 :
        return 5
    if n == 734 :
        return 5
    if n == 735 :
        return 5
    if n == 736 :
        return None
    if n == 737 :
        return 5
    if n == 738 :
        return 4
    if n == 739 :
        return 5
    if n == 740 :
        return 5
    if n == 741 :
        return 4
    if n == 742 :
        return None
    if n == 743 :
        return 5
    if n == 744 :
        return 4
    if n == 745 :
        return None
    if n == 746 :
        return 4
    if n == 747 :
        return 3
    if n == 748 :
        return None
    if n == 749 :
        return None
    if n == 750 :
        return 5
    if n == 751 :
        return None
    if n == 752 :
        return 4
    if n == 753 :
        return 4
    if n == 754 :
        return None
    if n == 755 :
        return 5
    if n == 756 :
        return 2
    if n == 757 :
        return 5
    if n == 758 :
        return None
    if n == 759 :
        return 4
    if n == 760 :
        return 5
    if n == 761 :
        return 4
    if n == 762 :
        return 4
    if n == 763 :
        return None
    if n == 764 :
        return 5
    if n == 765 :
        return 3
    if n == 766 :
        return 4
    if n == 767 :
        return None
    if n == 768 :
        return 4
    if n == 769 :
        return 5
    if n == 770 :
        return 4
    if n == 771 :
        return None
    if n == 772 :
        return 5
    if n == 773 :
        return None
    if n == 774 :
        return 4
    if n == 775 :
        return 3
    if n == 776 :
        return 6
    if n == 777 :
        return None
    if n == 778 :
        return 4
    if n == 779 :
        return 3
    if n == 780 :
        return 6
    if n == 781 :
        return None
    if n == 782 :
        return 5
    if n == 783 :
        return 3
    if n == 784 :
        return 6
    if n == 785 :
        return 4
    if n == 786 :
        return 6
    if n == 787 :
        return None
    if n == 788 :
        return 6
    if n == 789 :
        return 5
    if n == 790 :
        return 6
    if n == 791 :
        return 4
    if n == 792 :
        return 6
    if n == 793 :
        return 4
    if n == 794 :
        return 6
    if n == 795 :
        return 5
    if n == 796 :
        return 6
    if n == 797 :
        return 5
    if n == 798 :
        return 5
    if n == 799 :
        return 5
    if n == 800 :
        return 6
    if n == 801 :
        return 4
    if n == 802 :
        return 6
    if n == 803 :
        return 4
    if n == 804 :
        return 6
    if n == 805 :
        return 5
    if n == 806 :
        return 4
    if n == 807 :
        return 5
    if n == 808 :
        return 5
    if n == 809 :
        return 4
    if n == 810 :
        return 4
    if n == 811 :
        return 4
    if n == 812 :
        return None
    if n == 813 :
        return 5
    if n == 814 :
        return 4
    if n == 815 :
        return 5
    if n == 816 :
        return 5
    if n == 817 :
        return None
    if n == 818 :
        return 4
    if n == 819 :
        return 4
    if n == 820 :
        return 5
    if n == 821 :
        return 5
    if n == 822 :
        return None
    if n == 823 :
        return 3
    if n == 824 :
        return 4
    if n == 825 :
        return 5
    if n == 826 :
        return None
    if n == 827 :
        return 4
    if n == 828 :
        return 5
    if n == 829 :
        return None
    if n == 830 :
        return 5
    if n == 831 :
        return None
    if n == 832 :
        return None
    if n == 833 :
        return 5
    if n == 834 :
        return 4
    if n == 835 :
        return None
    if n == 836 :
        return 4
    if n == 837 :
        return 3
    if n == 838 :
        return None
    if n == 839 :
        return None
    if n == 840 :
        return 5
    if n == 841 :
        return 5
    if n == 842 :
        return 5
    if n == 843 :
        return 4
    if n == 844 :
        return None
    if n == 845 :
        return 5
    if n == 846 :
        return 4
    if n == 847 :
        return 5
    if n == 848 :
        return None
    if n == 849 :
        return 4
    if n == 850 :
        return 4
    if n == 851 :
        return 5
    if n == 852 :
        return 3
    if n == 853 :
        return None
    if n == 854 :
        return None
    if n == 855 :
        return 3
    if n == 856 :
        return 4
    if n == 857 :
        return None
    if n == 858 :
        return 4
    if n == 859 :
        return None
    if n == 860 :
        return 3
    if n == 861 :
        return 3
    if n == 862 :
        return None
    if n == 863 :
        return None
    if n == 864 :
        return 4
    if n == 865 :
        return 4
    if n == 866 :
        return None
    if n == 867 :
        return None
    if n == 868 :
        return None
    if n == 869 :
        return None
    if n == 870 :
        return None
    if n == 871 :
        return None
    if n == 872 :
        return None
    if n == 873 :
        return 3
    if n == 874 :
        return None
    if n == 875 :
        return None
    if n == 876 :
        return None
    if n == 877 :
        return None
    if n == 878 :
        return 4
    if n == 879 :
        return None
    if n == 880 :
        return None
    if n == 881 :
        return None
    if n == 882 :
        return 4
    if n == 883 :
        return None
    if n == 884 :
        return None
    if n == 885 :
        return None
    if n == 886 :
        return None
    if n == 887 :
        return None
    if n == 888 :
        return None
    if n == 889 :
        return None
    if n == 890 :
        return None
    if n == 891 :
        return 3
    if n == 892 :
        return None
    if n == 893 :
        return None
    if n == 894 :
        return None
    if n == 895 :
        return None
    if n == 896 :
        return None
    if n == 897 :
        return 4
    if n == 898 :
        return None
    if n == 899 :
        return 4
    if n == 900 :
        return None
    if n == 901 :
        return None
    if n == 902 :
        return None
    if n == 903 :
        return None
    if n == 904 :
        return None
    if n == 905 :
        return 4
    if n == 906 :
        return None
    if n == 907 :
        return 4
    if n == 908 :
        return None
    if n == 909 :
        return 4
    if n == 910 :
        return None
    if n == 911 :
        return None
    if n == 912 :
        return None
    if n == 913 :
        return None
    if n == 914 :
        return None
    if n == 915 :
        return 4
    if n == 916 :
        return None
    if n == 917 :
        return 4
    if n == 918 :
        return None
    if n == 919 :
        return 4
    if n == 920 :
        return None
    if n == 921 :
        return None
    if n == 922 :
        return None
    if n == 923 :
        return None
    if n == 924 :
        return None
    if n == 925 :
        return None
    if n == 926 :
        return None
    if n == 927 :
        return 4
    if n == 928 :
        return None
    if n == 929 :
        return None
    if n == 930 :
        return None
    if n == 931 :
        return None
    if n == 932 :
        return None
    if n == 933 :
        return None
    if n == 934 :
        return None
    if n == 935 :
        return None
    if n == 936 :
        return None
    if n == 937 :
        return None
    if n == 938 :
        return None
    if n == 939 :
        return None
    if n == 940 :
        return None
    if n == 941 :
        return None
    if n == 942 :
        return None
    if n == 943 :
        return None
    if n == 944 :
        return None
    if n == 945 :
        return None
    if n == 946 :
        return None
    if n == 947 :
        return None
    if n == 948 :
        return None
    if n == 949 :
        return None
    if n == 950 :
        return None
    if n == 951 :
        return 3
    if n == 952 :
        return None
    if n == 953 :
        return None
    if n == 954 :
        return None
    if n == 955 :
        return None
    if n == 956 :
        return None
    if n == 957 :
        return None
    if n == 958 :
        return None
    if n == 959 :
        return None
    if n == 960 :
        return None
    if n == 961 :
        return None
    if n == 962 :
        return None
    if n == 963 :
        return 3
    if n == 964 :
        return 3
    if n == 965 :
        return None
    if n == 966 :
        return None
    if n == 967 :
        return None
    if n == 968 :
        return 3
    if n == 969 :
        return None
    if n == 970 :
        return None
    if n == 971 :
        return None
    if n == 972 :
        return 3
    if n == 973 :
        return None
    if n == 974 :
        return None
    if n == 975 :
        return None
    if n == 976 :
        return None
    if n == 977 :
        return None
    if n == 978 :
        return None
    if n == 979 :
        return None
    if n == 980 :
        return None
    if n == 981 :
        return None
    if n == 982 :
        return None
    if n == 983 :
        return None
    if n == 984 :
        return None
    if n == 985 :
        return None
    if n == 986 :
        return None
    if n == 987 :
        return None
    if n == 988 :
        return None
    if n == 989 :
        return None
    if n == 990 :
        return None
    if n == 991 :
        return None
    if n == 992 :
        return None
    if n == 993 :
        return None
    if n == 994 :
        return None
    if n == 995 :
        return None
    if n == 996 :
        return None
    if n == 997 :
        return None
    if n == 998 :
        return None
    if n == 999 :
        return None
    if n == 1000 :
        return None

