from matplotlib import pyplot as plt


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072]
y = [0.09719, 0.12229, 0.13236, 0.13739, 0.13739, 0.15749, 0.16249, 0.16249, 0.16249, 0.17253, 0.2034, 0.20761, 0.20861, 0.22734, 0.22734, 0.23542, 0.2486, 0.26073, 0.26172, 0.27741, 0.31225, 0.34214, 0.34724, 0.34724, 0.35225, 0.35225, 0.37244, 0.37497, 0.37756, 0.38713, 0.39214, 0.3972, 0.40726, 0.40726, 0.41226, 0.41735, 0.43752, 0.44253, 0.4476, 0.45211, 0.45211, 0.46778, 0.48808, 0.49816, 0.51225, 0.52233, 0.52857, 0.53968, 0.54219, 0.54219, 0.54878, 0.55991, 0.56452, 0.56452, 0.56911, 0.57211, 0.57717, 0.60236, 0.61243, 0.62957, 0.6623, 0.67244, 0.71032, 0.71283, 0.71773, 0.73043, 0.73849, 0.74251, 0.75171, 0.75271, 0.75271, 0.75271, 0.75753, 0.7606, 0.76764, 0.77271, 0.77884, 0.79097, 0.79247, 0.79247, 0.79247, 0.80107, 0.82275, 0.83285, 0.86972, 0.87288, 0.89278, 0.90186, 0.90293, 1.02322, 1.02774, 1.09816, 1.10774, 1.13523, 1.13776, 1.14789, 1.14789, 1.17409, 1.17776, 1.21405, 1.21405, 1.21833, 1.22284, 1.22745, 1.23757, 1.24258, 1.24663, 1.24766, 1.24766, 1.25469, 1.25774, 1.26477, 1.27234, 1.27487, 1.30426, 1.32554, 1.32757, 1.34297, 1.34857, 1.35263, 1.49807, 1.5017, 1.50773, 1.51291, 1.54271, 1.54271, 1.63356, 1.63356, 1.63863, 1.64266, 1.64872, 1.68343, 1.68681, 1.68774, 1.68972, 1.69164, 1.69268, 1.69368, 1.69467, 1.69679, 1.69863, 1.70062, 1.70344, 1.70811, 1.71157, 1.71257, 1.71257, 1.71257, 1.73194, 1.73294, 1.73294, 1.74001, 1.74758, 1.74919, 1.75317, 1.76358, 1.77291, 1.77794, 1.77794, 1.78795, 1.79098, 1.793, 1.80296, 1.80794, 1.81096, 1.82328, 1.82328, 1.96754, 1.96854, 1.96854, 1.9736, 1.9736, 1.97773, 1.97773, 1.98781, 1.99751, 2.00119, 2.00368, 2.00779, 2.0128, 2.02927, 2.03027, 2.03779, 2.04594, 2.04846, 2.06618, 2.0727, 2.07779, 2.09241, 2.09241, 2.09546, 2.1057, 2.10669, 2.11072, 2.11617, 2.1177, 2.1177, 2.12781, 2.13795, 2.14783, 2.15581, 2.15783, 2.16284, 2.16284, 2.16796, 2.17203, 2.18566, 2.18887, 2.18987, 2.19281, 2.19414, 2.20295, 2.20757, 2.20948, 2.21621, 2.21773, 2.22511, 2.23138, 2.24806, 2.25612, 2.26267, 2.2782, 2.48813, 2.49266, 2.49266, 2.50282, 2.5117, 2.5127, 2.52279, 2.54258, 2.56276, 2.57284, 2.58295, 2.58812, 2.58965, 2.59268, 2.59268, 2.59776, 2.61188, 2.61243, 2.61443, 2.61443, 2.79401, 2.79753, 2.79753, 2.80206, 2.80411, 2.80764, 2.82442, 2.82442, 2.82442, 2.83249, 2.83451, 2.83755, 2.84508, 2.84763, 2.85467, 2.85769, 2.86274, 2.86783, 2.86783, 2.87589, 2.89276, 2.8933, 2.91223, 2.91383, 2.91885, 2.92097, 2.92197, 2.92757, 2.92757, 2.92757, 2.93571, 2.93773, 2.93773, 2.9626, 2.96615, 2.97473, 2.97524, 2.97779, 2.9828, 2.9828, 2.98736, 2.99744, 2.99744, 3.01507, 3.02771, 3.03103, 3.03217, 3.03217, 3.03521, 3.03775, 3.04275, 3.04731, 3.05231, 3.06237, 3.0654, 3.0886, 3.09217, 3.10119, 3.43764, 3.44894, 3.45098, 3.45308, 3.47106, 3.47309, 3.50212, 3.51762, 3.52425, 3.52778, 3.53334, 3.53793, 3.53793, 3.54756, 3.55158, 3.55362, 3.56375, 3.56375, 3.56777, 3.582, 3.5947, 3.60208, 3.60419, 3.60659, 3.735, 3.735, 3.73943, 3.73943, 3.74752, 3.75253, 3.75306, 3.75765, 3.75765, 3.75765, 3.76536, 3.76536, 3.77745, 4.12556, 4.13163, 4.13301, 4.13401, 4.13769, 4.13983, 4.14187, 4.14187, 4.1479, 4.15197, 4.15804, 4.1621, 4.1621, 4.1621, 4.1702, 4.17223, 4.17223, 4.17779, 4.18032, 4.18234, 4.18787, 4.19039, 4.19245, 4.19245, 4.19789, 4.20072, 4.2018, 4.20379, 4.20783, 4.21089, 4.21445, 4.21445, 4.25763, 4.25814, 4.26052, 4.26451, 4.2739, 4.28193, 4.28396, 4.28798, 4.29407, 4.29407, 4.52911, 4.53198, 4.53672, 4.55541, 4.60773, 4.61507, 4.62345, 4.62805, 4.63107, 4.64436, 4.64766, 4.6572, 4.6664, 4.67201, 4.68806, 4.68909, 4.69403, 4.69978, 4.71084, 4.72128, 4.7248, 4.72699, 4.75281, 4.76315, 4.77977, 4.79026, 4.82001, 4.82101, 4.82201, 4.82389, 4.82754, 4.83502, 4.84104, 4.84413, 4.84513, 4.84996, 4.8535, 4.85502, 4.85785, 4.8605, 4.8625, 4.87536, 4.89026, 4.89325, 4.89933, 4.90471, 4.9077, 4.92018, 4.9574, 4.96775, 4.97008, 4.97575, 4.97983, 4.98083, 4.98283, 4.99775, 5.00305, 5.23887, 5.24228, 5.25598, 5.25809, 5.26801, 5.27778, 5.29884, 5.31091, 5.3281, 5.3339, 5.34166, 5.67704, 5.68156, 5.68801, 5.69363, 5.69666, 5.69898, 5.70661, 5.70763, 5.71427, 5.72216, 5.7282, 5.7312, 5.73634, 5.74171, 5.74171, 5.75052, 5.75826, 5.76026, 5.76756, 6.02253, 6.02735, 6.0302, 6.03419, 6.0413, 6.04387, 6.04614, 6.05236, 6.05391, 6.05809, 6.06008, 6.18179, 6.18279, 6.19042, 6.19295, 6.19604, 6.20004, 6.21124, 6.21423, 6.21776, 6.22325, 6.22955, 6.23254, 6.23354, 6.36588, 6.37658, 6.37861, 6.38175, 6.38564, 6.4147, 6.41996, 6.51871, 6.51998, 6.5213, 6.5258, 6.52998, 6.53098, 6.53911, 6.54323, 6.54423, 6.54722, 6.56396, 6.57097, 6.57698, 6.58416, 6.58624, 6.59211, 6.60103, 6.60354, 6.60865, 6.61882, 6.61983, 6.62284, 6.62583, 6.63271, 6.63566, 6.64192, 6.64595, 6.65394, 6.65594, 6.65893, 6.66092, 6.83145, 6.8335, 6.83549, 6.83649, 6.83749, 6.8415, 6.84504, 6.85478, 6.85628, 6.85628, 6.8638, 6.86778, 6.86914, 6.87534, 6.88017, 6.91625, 6.94382, 6.95072, 6.9606, 6.97001, 6.97201, 6.98654, 6.99642, 7.00045, 7.00245, 7.00444, 7.00952, 7.01048, 7.01348, 7.02648, 7.02862, 7.03484, 7.03554, 7.04953, 7.05053, 7.05452, 7.24583, 7.25285, 7.25983, 7.27277, 7.2849, 7.29271, 7.2977, 7.30274, 7.45482, 7.45783, 7.46083, 7.46183, 7.46662, 7.46794, 7.4729, 7.47641, 7.4781, 7.48091, 7.50085, 7.50551, 7.50806, 7.51793, 7.66984, 7.67284, 7.67483, 7.68103, 7.68786, 7.69384, 7.69789, 7.70404, 7.70591, 7.80002, 7.80281, 7.80381, 7.8068, 7.81209, 7.82581, 7.82762, 7.82829, 7.82926, 7.83182, 7.84706, 7.85818, 7.86021, 7.86624, 7.86915, 7.87117, 7.87411, 7.87913, 7.88126, 7.88423, 7.88929, 7.99881, 7.99981, 8.0028, 8.00854, 8.01359, 8.01665, 8.01962, 8.02261, 8.03013, 8.03419, 8.03628, 8.04238, 8.04891, 8.04991, 8.27141, 8.34704, 8.35702, 8.364, 8.365, 8.44479, 8.44829, 8.45528, 8.45779, 8.46229, 8.46229, 8.4724, 8.4734, 8.47539, 8.50789, 8.56567, 8.57078, 8.57377, 8.57876, 8.72992, 8.73183, 8.73583, 8.86374, 8.87719, 8.88824, 8.89322, 8.91025, 8.91718, 8.91918, 9.01501, 9.017, 9.019, 9.01999, 9.01999, 9.02955, 9.03154, 9.12801, 9.12852, 9.13052, 9.13603, 9.13902, 9.145, 9.15748, 9.30483, 9.30898, 9.31204, 9.31303, 9.31702, 9.32214, 9.32912, 9.34161, 9.34708, 9.40073, 9.40173, 9.40971, 9.41071, 9.4124, 9.4179, 9.42188, 9.43286, 9.43385, 9.43684, 9.43996, 9.44195, 9.44295, 9.44794, 9.45492, 9.4639, 9.46589, 9.46689, 9.46789, 9.47088, 9.47188, 9.47786, 9.48285, 9.49282, 9.49482, 9.50381, 9.50681, 9.51939, 9.52118, 9.52318, 9.52517, 9.52717, 9.53315, 9.53814, 9.53921, 9.54213, 9.54412, 9.54512, 9.57561, 9.57761, 9.5826, 9.58659, 9.60158, 9.60258, 9.60557, 9.60656, 9.61055, 9.61454, 9.61654, 9.62252, 9.62709, 9.62809, 9.63308, 9.64305, 9.64505, 9.64804, 9.65802, 9.67249, 9.67419, 9.67716, 9.69381, 9.69544, 9.70168, 9.71005, 9.7141, 9.72321, 9.73019, 9.73418, 9.73817, 9.74515, 9.75612, 9.75863, 9.98275, 9.98375, 9.98692, 9.99757, 9.99908, 10.00471, 10.01241, 10.01594, 10.02773, 10.03172, 10.03829, 10.04782, 10.0563, 10.05988, 10.0729, 10.0777, 10.0787, 10.07969, 10.0867, 10.2959, 10.30388, 10.31186, 10.31285, 10.31485, 10.31585, 10.32099, 10.33794, 10.35004, 10.35303, 10.35773, 10.36569, 10.37041, 10.3724, 10.3734, 10.37839, 10.38138, 10.38488, 10.38488, 10.39536, 10.40534, 10.54049, 10.54178, 10.54477, 10.55303, 10.5697, 10.57976, 10.58594, 10.59003, 10.69775, 10.70074, 10.70274, 10.70274, 10.70374, 10.71072, 10.71271, 10.71371, 10.71821, 10.7212, 10.72519, 10.72918, 10.73816, 10.74115, 10.74414, 10.74813, 10.75611, 10.7581, 10.76209, 10.76309, 10.76708, 10.76908, 10.79103, 10.79345, 10.79526, 10.8036, 10.80759, 10.81558, 10.81662, 10.82207, 10.83205, 10.84518, 10.84663, 10.84896, 10.85594, 10.85945, 10.98478, 10.98977, 10.99077, 10.99176, 10.99276, 10.99575, 10.99675, 11.01172, 11.01969, 11.02568, 11.03565, 11.04961, 11.05659, 11.05813, 11.06065, 11.06163, 11.06163, 11.06761, 11.06761, 11.09012, 11.09311, 11.23763, 11.24661, 11.25318, 11.25617, 11.25826, 11.27239, 11.27538, 11.28237, 11.2845, 11.28735, 11.28886, 11.29164, 11.29317, 11.29317, 11.2945, 11.43445, 11.44243, 11.54146, 11.54146, 11.55144, 11.55296, 11.55495, 11.55695, 11.56692, 11.57091, 11.69102, 11.7155, 11.72248, 11.72448, 11.72847, 11.73545, 11.74442, 11.7564, 11.75939, 11.76338, 11.7673, 11.76979, 11.78019, 11.78319, 11.78717, 11.79256, 11.79815, 11.80513, 11.80712, 11.81033, 11.81233, 11.81732, 11.82438, 11.82687, 11.82887, 11.83086, 11.83186, 11.84087, 11.84486, 11.85088, 11.85188, 11.8709, 11.88843, 11.88895, 11.89492, 12.07694, 12.08006, 12.08107, 12.08406, 12.08506, 12.09005, 12.09204, 12.09703, 12.10102, 12.11, 12.11199, 12.11798, 12.24785, 12.24837, 12.25135, 12.26583, 12.26935, 12.27136, 12.2824, 12.44814, 12.45014, 12.45129, 12.45417, 12.4562, 12.4572, 12.45924, 12.46323, 12.46562, 12.46912, 12.47211, 12.47511, 12.48209, 12.48408, 12.48608, 12.48807, 12.50204, 12.5225, 12.53013, 12.56377, 12.56576, 12.58525, 12.59313, 12.59345, 12.59445, 12.59744, 12.60343, 12.61041, 12.61141, 12.73756, 12.73955, 12.74653, 12.75052, 12.75252, 12.75551, 12.7595, 12.76848, 12.77352, 12.77452, 12.77651, 12.77651, 12.77849, 12.781, 12.78849, 12.79348, 12.80246, 12.85702, 12.96531, 12.9733, 12.98052, 12.98204, 12.98502, 12.99604, 12.99802, 13.00343, 13.07929, 13.0813, 13.0823, 13.08429, 13.08828, 13.08928, 13.09789, 13.09889, 13.0999, 13.10141, 13.1034, 13.10639, 13.12248, 13.14002, 13.14152, 13.14352, 13.14551, 13.15005, 13.15309, 13.16007, 13.1661, 13.17508, 13.22689, 13.23587, 13.24237, 13.26062, 13.2656, 13.2656, 13.28211, 13.28367, 13.28624, 13.2897, 13.2962, 13.30598, 13.31431, 13.3203, 13.32329, 13.32669, 13.33498, 13.34052, 13.34811, 13.3501, 13.35616, 13.3612, 13.36313, 13.36467, 13.37594, 13.37691, 13.37791, 13.37891, 13.4163, 13.41929, 13.42129, 13.42229, 13.43286, 13.47522, 13.48302, 13.48796, 13.49796, 13.51148, 13.5295, 13.5421, 13.54985, 13.55496, 13.55737, 13.55833, 13.56435, 13.58553, 13.58652, 13.60927, 13.61687, 13.62518, 13.64833, 13.65817, 13.67112, 13.6761, 13.79986, 13.89951, 13.97541]

# Function to plot 
plt.plot(x,y) 

plt.xlabel('Image Count')
plt.ylabel('Time (seconds)')

plt.title('Multi Thread Execution')
# function to show the plot 
plt.show() 



"""
l = [[1, 0.09719], [2, 0.12229], [3, 0.13236], [4, 0.13739], [5, 0.13739], [6, 0.15749], [7, 0.16249], [8, 0.16249], [9, 0.16249], [10, 0.17253], [11, 0.2034], [12, 0.20761], [13, 0.20861], [14, 0.22734], [15, 0.22734], [16, 0.23542], [17, 0.2486], [18, 0.26073], [19, 0.26172], [20, 0.27741], [21, 0.31225], [22, 0.34214], [23, 0.34724], [24, 0.34724], [25, 0.35225], [26, 0.35225], [27, 0.37244], [28, 0.37497], [29, 0.37756], [30, 0.38713], [31, 0.39214], [32, 0.3972], [33, 0.40726], [34, 0.40726], [35, 0.41226], [36, 0.41735], [37, 0.43752], [38, 0.44253], [39, 0.4476], [40, 0.45211], [41, 0.45211], [42, 0.46778], [43, 0.48808], [44, 0.49816], [45, 0.51225], [46, 0.52233], [47, 0.52857], [48, 0.53968], [49, 0.54219], [50, 0.54219], [51, 0.54878], [52, 0.55991], [53, 0.56452], [54, 0.56452], [55, 0.56911], [56, 0.57211], [57, 0.57717], [58, 0.60236], [59, 0.61243], [60, 0.62957], [61, 0.6623], [62, 0.67244], [63, 0.71032], [64, 0.71283], [65, 0.71773], [66, 0.73043], [67, 0.73849], [68, 0.74251], [69, 0.75171], [70, 0.75271], [71, 0.75271], [72, 0.75271], [73, 0.75753], [74, 0.7606], [75, 0.76764], [76, 0.77271], [77, 0.77884], [78, 0.79097], [79, 0.79247], [80, 0.79247], [81, 0.79247], [82, 0.80107], [83, 0.82275], [84, 0.83285], [85, 0.86972], [86, 0.87288], [87, 0.89278], [88, 0.90186], [89, 0.90293], [90, 1.02322], [91, 1.02774], [92, 1.09816], [93, 1.10774], [94, 1.13523], [95, 1.13776], [96, 1.14789], [97, 1.14789], [98, 1.17409], [99, 1.17776], [100, 1.21405], [101, 1.21405], [102, 1.21833], [103, 1.22284], [104, 1.22745], [105, 1.23757], [106, 1.24258], [107, 1.24663], [108, 1.24766], [109, 1.24766], [110, 1.25469], [111, 1.25774], [112, 1.26477], [113, 1.27234], [114, 1.27487], [115, 1.30426], [116, 1.32554], [117, 1.32757], [118, 1.34297], [119, 1.34857], [120, 1.35263], [121, 1.49807], [122, 1.5017], [123, 1.50773], [124, 1.51291], [125, 1.54271], [126, 1.54271], [127, 1.63356], [128, 1.63356], [129, 1.63863], [130, 1.64266], [131, 1.64872], [132, 1.68343], [133, 1.68681], [134, 1.68774], [135, 1.68972], [136, 1.69164], [137, 1.69268], [138, 1.69368], [139, 1.69467], [140, 1.69679], [141, 1.69863], [142, 1.70062], [143, 1.70344], [144, 1.70811], [145, 1.71157], [146, 1.71257], [147, 1.71257], [148, 1.71257], [149, 1.73194], [150, 1.73294], [151, 1.73294], [152, 1.74001], [153, 1.74758], [154, 1.74919], [155, 1.75317], [156, 1.76358], [157, 1.77291], [158, 1.77794], [159, 1.77794], [160, 1.78795], [161, 1.79098], [162, 1.793], [163, 1.80296], [164, 1.80794], [165, 1.81096], [166, 1.82328], [167, 1.82328], [168, 1.96754], [169, 1.96854], [170, 1.96854], [171, 1.9736], [172, 1.9736], [173, 1.97773], [174, 1.97773], [175, 1.98781], [176, 1.99751], [177, 2.00119], [178, 2.00368], [179, 2.00779], [180, 2.0128], [181, 2.02927], [182, 2.03027], [183, 2.03779], [184, 2.04594], [185, 2.04846], [186, 2.06618], [187, 2.0727], [188, 2.07779], [189, 2.09241], [190, 2.09241], [191, 2.09546], [192, 2.1057], [193, 2.10669], [194, 2.11072], [195, 2.11617], [196, 2.1177], [197, 2.1177], [198, 2.12781], [199, 2.13795], [200, 2.14783], [201, 2.15581], [202, 2.15783], [203, 2.16284], [204, 2.16284], [205, 2.16796], [206, 2.17203], [207, 2.18566], [208, 2.18887], [209, 2.18987], [210, 2.19281], [211, 2.19414], [212, 2.20295], [213, 2.20757], [214, 2.20948], [215, 2.21621], [216, 2.21773], [217, 2.22511], [218, 2.23138], [219, 2.24806], [220, 2.25612], [221, 2.26267], [222, 2.2782], [223, 2.48813], [224, 2.49266], [225, 2.49266], [226, 2.50282], [227, 2.5117], [228, 2.5127], [229, 2.52279], [230, 2.54258], [231, 2.56276], [232, 2.57284], [233, 2.58295], [234, 2.58812], [235, 2.58965], [236, 2.59268], [237, 2.59268], [238, 2.59776], [239, 2.61188], [240, 2.61243], [241, 2.61443], [242, 2.61443], [243, 2.79401], [244, 2.79753], [245, 2.79753], [246, 2.80206], [247, 2.80411], [248, 2.80764], [249, 2.82442], [250, 2.82442], [251, 2.82442], [252, 2.83249], [253, 2.83451], [254, 2.83755], [255, 2.84508], [256, 2.84763], [257, 2.85467], [258, 2.85769], [259, 2.86274], [260, 2.86783], [261, 2.86783], [262, 2.87589], [263, 2.89276], [264, 2.8933], [265, 2.91223], [266, 2.91383], [267, 2.91885], [268, 2.92097], [269, 2.92197], [270, 2.92757], [271, 2.92757], [272, 2.92757], [273, 2.93571], [274, 2.93773], [275, 2.93773], [276, 2.9626], [277, 2.96615], [278, 2.97473], [279, 2.97524], [280, 2.97779], [281, 2.9828], [282, 2.9828], [283, 2.98736], [284, 2.99744], [285, 2.99744], [286, 3.01507], [287, 3.02771], [288, 3.03103], [289, 3.03217], [290, 3.03217], [291, 3.03521], [292, 3.03775], [293, 3.04275], [294, 3.04731], [295, 3.05231], [296, 3.06237], [297, 3.0654], [298, 3.0886], [299, 3.09217], [300, 3.10119], [301, 3.43764], [302, 3.44894], [303, 3.45098], [304, 3.45308], [305, 3.47106], [306, 3.47309], [307, 3.50212], [308, 3.51762], [309, 3.52425], [310, 3.52778], [311, 3.53334], [312, 3.53793], [313, 3.53793], [314, 3.54756], [315, 3.55158], [316, 3.55362], [317, 3.56375], [318, 3.56375], [319, 3.56777], [320, 3.582], [321, 3.5947], [322, 3.60208], [323, 3.60419], [324, 3.60659], [325, 3.735], [326, 3.735], [327, 3.73943], [328, 3.73943], [329, 3.74752], [330, 3.75253], [331, 3.75306], [332, 3.75765], [333, 3.75765], [334, 3.75765], [335, 3.76536], [336, 3.76536], [337, 3.77745], [338, 4.12556], [339, 4.13163], [340, 4.13301], [341, 4.13401], [342, 4.13769], [343, 4.13983], [344, 4.14187], [345, 4.14187], [346, 4.1479], [347, 4.15197], [348, 4.15804], [349, 4.1621], [350, 4.1621], [351, 4.1621], [352, 4.1702], [353, 4.17223], [354, 4.17223], [355, 4.17779], [356, 4.18032], [357, 4.18234], [358, 4.18787], [359, 4.19039], [360, 4.19245], [361, 4.19245], [362, 4.19789], [363, 4.20072], [364, 4.2018], [365, 4.20379], [366, 4.20783], [367, 4.21089], [368, 4.21445], [369, 4.21445], [370, 4.25763], [371, 4.25814], [372, 4.26052], [373, 4.26451], [374, 4.2739], [375, 4.28193], [376, 4.28396], [377, 4.28798], [378, 4.29407], [379, 4.29407], [380, 4.52911], [381, 4.53198], [382, 4.53672], [383, 4.55541], [384, 4.60773], [385, 4.61507], [386, 4.62345], [387, 4.62805], [388, 4.63107], [389, 4.64436], [390, 4.64766], [391, 4.6572], [392, 4.6664], [393, 4.67201], [394, 4.68806], [395, 4.68909], [396, 4.69403], [397, 4.69978], [398, 4.71084], [399, 4.72128], [400, 4.7248], [401, 4.72699], [402, 4.75281], [403, 4.76315], [404, 4.77977], [405, 4.79026], [406, 4.82001], [407, 4.82101], [408, 4.82201], [409, 4.82389], [410, 4.82754], [411, 4.83502], [412, 4.84104], [413, 4.84413], [414, 4.84513], [415, 4.84996], [416, 4.8535], [417, 4.85502], [418, 4.85785], [419, 4.8605], [420, 4.8625], [421, 4.87536], [422, 4.89026], [423, 4.89325], [424, 4.89933], [425, 4.90471], [426, 4.9077], [427, 4.92018], [428, 4.9574], [429, 4.96775], [430, 4.97008], [431, 4.97575], [432, 4.97983], [433, 4.98083], [434, 4.98283], [435, 4.99775], [436, 5.00305], [437, 5.23887], [438, 5.24228], [439, 5.25598], [440, 5.25809], [441, 5.26801], [442, 5.27778], [443, 5.29884], [444, 5.31091], [445, 5.3281], [446, 5.3339], [447, 5.34166], [448, 5.67704], [449, 5.68156], [450, 5.68801], [451, 5.69363], [452, 5.69666], [453, 5.69898], [454, 5.70661], [455, 5.70763], [456, 5.71427], [457, 5.72216], [458, 5.7282], [459, 5.7312], [460, 5.73634], [461, 5.74171], [462, 5.74171], [463, 5.75052], [464, 5.75826], [465, 5.76026], [466, 5.76756], [467, 6.02253], [468, 6.02735], [469, 6.0302], [470, 6.03419], [471, 6.0413], [472, 6.04387], [473, 6.04614], [474, 6.05236], [475, 6.05391], [476, 6.05809], [477, 6.06008], [478, 6.18179], [479, 6.18279], [480, 6.19042], [481, 6.19295], [482, 6.19604], [483, 6.20004], [484, 6.21124], [485, 6.21423], [486, 6.21776], [487, 6.22325], [488, 6.22955], [489, 6.23254], [490, 6.23354], [491, 6.36588], [492, 6.37658], [493, 6.37861], [494, 6.38175], [495, 6.38564], [496, 6.4147], [497, 6.41996], [498, 6.51871], [499, 6.51998], [500, 6.5213], [501, 6.5258], [502, 6.52998], [503, 6.53098], [504, 6.53911], [505, 6.54323], [506, 6.54423], [507, 6.54722], [508, 6.56396], [509, 6.57097], [510, 6.57698], [511, 6.58416], [512, 6.58624], [513, 6.59211], [514, 6.60103], [515, 6.60354], [516, 6.60865], [517, 6.61882], [518, 6.61983], [519, 6.62284], [520, 6.62583], [521, 6.63271], [522, 6.63566], [523, 6.64192], [524, 6.64595], [525, 6.65394], [526, 6.65594], [527, 6.65893], [528, 6.66092], [529, 6.83145], [530, 6.8335], [531, 6.83549], [532, 6.83649], [533, 6.83749], [534, 6.8415], [535, 6.84504], [536, 6.85478], [537, 6.85628], [538, 6.85628], [539, 6.8638], [540, 6.86778], [541, 6.86914], [542, 6.87534], [543, 6.88017], [544, 6.91625], [545, 6.94382], [546, 6.95072], [547, 6.9606], [548, 6.97001], [549, 6.97201], [550, 6.98654], [551, 6.99642], [552, 7.00045], [553, 7.00245], [554, 7.00444], [555, 7.00952], [556, 7.01048], [557, 7.01348], [558, 7.02648], [559, 7.02862], [560, 7.03484], [561, 7.03554], [562, 7.04953], [563, 7.05053], [564, 7.05452], [565, 7.24583], [566, 7.25285], [567, 7.25983], [568, 7.27277], [569, 7.2849], [570, 7.29271], [571, 7.2977], [572, 7.30274], [573, 7.45482], [574, 7.45783], [575, 7.46083], [576, 7.46183], [577, 7.46662], [578, 7.46794], [579, 7.4729], [580, 7.47641], [581, 7.4781], [582, 7.48091], [583, 7.50085], [584, 7.50551], [585, 7.50806], [586, 7.51793], [587, 7.66984], [588, 7.67284], [589, 7.67483], [590, 7.68103], [591, 7.68786], [592, 7.69384], [593, 7.69789], [594, 7.70404], [595, 7.70591], [596, 7.80002], [597, 7.80281], [598, 7.80381], [599, 7.8068], [600, 7.81209], [601, 7.82581], [602, 7.82762], [603, 7.82829], [604, 7.82926], [605, 7.83182], [606, 7.84706], [607, 7.85818], [608, 7.86021], [609, 7.86624], [610, 7.86915], [611, 7.87117], [612, 7.87411], [613, 7.87913], [614, 7.88126], [615, 7.88423], [616, 7.88929], [617, 7.99881], [618, 7.99981], [619, 8.0028], [620, 8.00854], [621, 8.01359], [622, 8.01665], [623, 8.01962], [624, 8.02261], [625, 8.03013], [626, 8.03419], [627, 8.03628], [628, 8.04238], [629, 8.04891], [630, 8.04991], [631, 8.27141], [632, 8.34704], [633, 8.35702], [634, 8.364], [635, 8.365], [636, 8.44479], [637, 8.44829], [638, 8.45528], [639, 8.45779], [640, 8.46229], [641, 8.46229], [642, 8.4724], [643, 8.4734], [644, 8.47539], [645, 8.50789], [646, 8.56567], [647, 8.57078], [648, 8.57377], [649, 8.57876], [650, 8.72992], [651, 8.73183], [652, 8.73583], [653, 8.86374], [654, 8.87719], [655, 8.88824], [656, 8.89322], [657, 8.91025], [658, 8.91718], [659, 8.91918], [660, 9.01501], [661, 9.017], [662, 9.019], [663, 9.01999], [664, 9.01999], [665, 9.02955], [666, 9.03154], [667, 9.12801], [668, 9.12852], [669, 9.13052], [670, 9.13603], [671, 9.13902], [672, 9.145], [673, 9.15748], [674, 9.30483], [675, 9.30898], [676, 9.31204], [677, 9.31303], [678, 9.31702], [679, 9.32214], [680, 9.32912], [681, 9.34161], [682, 9.34708], [683, 9.40073], [684, 9.40173], [685, 9.40971], [686, 9.41071], [687, 9.4124], [688, 9.4179], [689, 9.42188], [690, 9.43286], [691, 9.43385], [692, 9.43684], [693, 9.43996], [694, 9.44195], [695, 9.44295], [696, 9.44794], [697, 9.45492], [698, 9.4639], [699, 9.46589], [700, 9.46689], [701, 9.46789], [702, 9.47088], [703, 9.47188], [704, 9.47786], [705, 9.48285], [706, 9.49282], [707, 9.49482], [708, 9.50381], [709, 9.50681], [710, 9.51939], [711, 9.52118], [712, 9.52318], [713, 9.52517], [714, 9.52717], [715, 9.53315], [716, 9.53814], [717, 9.53921], [718, 9.54213], [719, 9.54412], [720, 9.54512], [721, 9.57561], [722, 9.57761], [723, 9.5826], [724, 9.58659], [725, 9.60158], [726, 9.60258], [727, 9.60557], [728, 9.60656], [729, 9.61055], [730, 9.61454], [731, 9.61654], [732, 9.62252], [733, 9.62709], [734, 9.62809], [735, 9.63308], [736, 9.64305], [737, 9.64505], [738, 9.64804], [739, 9.65802], [740, 9.67249], [741, 9.67419], [742, 9.67716], [743, 9.69381], [744, 9.69544], [745, 9.70168], [746, 9.71005], [747, 9.7141], [748, 9.72321], [749, 9.73019], [750, 9.73418], [751, 9.73817], [752, 9.74515], [753, 9.75612], [754, 9.75863], [755, 9.98275], [756, 9.98375], [757, 9.98692], [758, 9.99757], [759, 9.99908], [760, 10.00471], [761, 10.01241], [762, 10.01594], [763, 10.02773], [764, 10.03172], [765, 10.03829], [766, 10.04782], [767, 10.0563], [768, 10.05988], [769, 10.0729], [770, 10.0777], [771, 10.0787], [772, 10.07969], [773, 10.0867], [774, 10.2959], [775, 10.30388], [776, 10.31186], [777, 10.31285], [778, 10.31485], [779, 10.31585], [780, 10.32099], [781, 10.33794], [782, 10.35004], [783, 10.35303], [784, 10.35773], [785, 10.36569], [786, 10.37041], [787, 10.3724], [788, 10.3734], [789, 10.37839], [790, 10.38138], [791, 10.38488], [792, 10.38488], [793, 10.39536], [794, 10.40534], [795, 10.54049], [796, 10.54178], [797, 10.54477], [798, 10.55303], [799, 10.5697], [800, 10.57976], [801, 10.58594], [802, 10.59003], [803, 10.69775], [804, 10.70074], [805, 10.70274], [806, 10.70274], [807, 10.70374], [808, 10.71072], [809, 10.71271], [810, 10.71371], [811, 10.71821], [812, 10.7212], [813, 10.72519], [814, 10.72918], [815, 10.73816], [816, 10.74115], [817, 10.74414], [818, 10.74813], [819, 10.75611], [820, 10.7581], [821, 10.76209], [822, 10.76309], [823, 10.76708], [824, 10.76908], [825, 10.79103], [826, 10.79345], [827, 10.79526], [828, 10.8036], [829, 10.80759], [830, 10.81558], [831, 10.81662], [832, 10.82207], [833, 10.83205], [834, 10.84518], [835, 10.84663], [836, 10.84896], [837, 10.85594], [838, 10.85945], [839, 10.98478], [840, 10.98977], [841, 10.99077], [842, 10.99176], [843, 10.99276], [844, 10.99575], [845, 10.99675], [846, 11.01172], [847, 11.01969], [848, 11.02568], [849, 11.03565], [850, 11.04961], [851, 11.05659], [852, 11.05813], [853, 11.06065], [854, 11.06163], [855, 11.06163], [856, 11.06761], [857, 11.06761], [858, 11.09012], [859, 11.09311], [860, 11.23763], [861, 11.24661], [862, 11.25318], [863, 11.25617], [864, 11.25826], [865, 11.27239], [866, 11.27538], [867, 11.28237], [868, 11.2845], [869, 11.28735], [870, 11.28886], [871, 11.29164], [872, 11.29317], [873, 11.29317], [874, 11.2945], [875, 11.43445], [876, 11.44243], [877, 11.54146], [878, 11.54146], [879, 11.55144], [880, 11.55296], [881, 11.55495], [882, 11.55695], [883, 11.56692], [884, 11.57091], [885, 11.69102], [886, 11.7155], [887, 11.72248], [888, 11.72448], [889, 11.72847], [890, 11.73545], [891, 11.74442], [892, 11.7564], [893, 11.75939], [894, 11.76338], [895, 11.7673], [896, 11.76979], [897, 11.78019], [898, 11.78319], [899, 11.78717], [900, 11.79256], [901, 11.79815], [902, 11.80513], [903, 11.80712], [904, 11.81033], [905, 11.81233], [906, 11.81732], [907, 11.82438], [908, 11.82687], [909, 11.82887], [910, 11.83086], [911, 11.83186], [912, 11.84087], [913, 11.84486], [914, 11.85088], [915, 11.85188], [916, 11.8709], [917, 11.88843], [918, 11.88895], [919, 11.89492], [920, 12.07694], [921, 12.08006], [922, 12.08107], [923, 12.08406], [924, 12.08506], [925, 12.09005], [926, 12.09204], [927, 12.09703], [928, 12.10102], [929, 12.11], [930, 12.11199], [931, 12.11798], [932, 12.24785], [933, 12.24837], [934, 12.25135], [935, 12.26583], [936, 12.26935], [937, 12.27136], [938, 12.2824], [939, 12.44814], [940, 12.45014], [941, 12.45129], [942, 12.45417], [943, 12.4562], [944, 12.4572], [945, 12.45924], [946, 12.46323], [947, 12.46562], [948, 12.46912], [949, 12.47211], [950, 12.47511], [951, 12.48209], [952, 12.48408], [953, 12.48608], [954, 12.48807], [955, 12.50204], [956, 12.5225], [957, 12.53013], [958, 12.56377], [959, 12.56576], [960, 12.58525], [961, 12.59313], [962, 12.59345], [963, 12.59445], [964, 12.59744], [965, 12.60343], [966, 12.61041], [967, 12.61141], [968, 12.73756], [969, 12.73955], [970, 12.74653], [971, 12.75052], [972, 12.75252], [973, 12.75551], [974, 12.7595], [975, 12.76848], [976, 12.77352], [977, 12.77452], [978, 12.77651], [979, 12.77651], [980, 12.77849], [981, 12.781], [982, 12.78849], [983, 12.79348], [984, 12.80246], [985, 12.85702], [986, 12.96531], [987, 12.9733], [988, 12.98052], [989, 12.98204], [990, 12.98502], [991, 12.99604], [992, 12.99802], [993, 13.00343], [994, 13.07929], [995, 13.0813], [996, 13.0823], [997, 13.08429], [998, 13.08828], [999, 13.08928], [1000, 13.09789], [1001, 13.09889], [1002, 13.0999], [1003, 13.10141], [1004, 13.1034], [1005, 13.10639], [1006, 13.12248], [1007, 13.14002], [1008, 13.14152], [1009, 13.14352], [1010, 13.14551], [1011, 13.15005], [1012, 13.15309], [1013, 13.16007], [1014, 13.1661], [1015, 13.17508], [1016, 13.22689], [1017, 13.23587], [1018, 13.24237], [1019, 13.26062], [1020, 13.2656], [1021, 13.2656], [1022, 13.28211], [1023, 13.28367], [1024, 13.28624], [1025, 13.2897], [1026, 13.2962], [1027, 13.30598], [1028, 13.31431], [1029, 13.3203], [1030, 13.32329], [1031, 13.32669], [1032, 13.33498], [1033, 13.34052], [1034, 13.34811], [1035, 13.3501], [1036, 13.35616], [1037, 13.3612], [1038, 13.36313], [1039, 13.36467], [1040, 13.37594], [1041, 13.37691], [1042, 13.37791], [1043, 13.37891], [1044, 13.4163], [1045, 13.41929], [1046, 13.42129], [1047, 13.42229], [1048, 13.43286], [1049, 13.47522], [1050, 13.48302], [1051, 13.48796], [1052, 13.49796], [1053, 13.51148], [1054, 13.5295], [1055, 13.5421], [1056, 13.54985], [1057, 13.55496], [1058, 13.55737], [1059, 13.55833], [1060, 13.56435], [1061, 13.58553], [1062, 13.58652], [1063, 13.60927], [1064, 13.61687], [1065, 13.62518], [1066, 13.64833], [1067, 13.65817], [1068, 13.67112], [1069, 13.6761], [1070, 13.79986], [1071, 13.89951], [1072, 13.97541]]
ll= []
c1 = 0
for x in l:
        try:
                if x[0] is not None:
                        ll.append(x)
        except:
                pass
x = []
y = []
for i in ll:
        x.append(i[0])
        y.append(i[1])

# x is imae count
# y is time stamp
print(x)
print(y)
z = list(y)
y.sort()
print(y)
print(z==y)
"""
