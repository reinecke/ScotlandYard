from SYPlayer import *
def board():
		gameBoard = {}
		gameBoard[0] = {}
		gameBoard[1] = 		{9: [SYTAXI, SYBLACK],
							8: [SYTAXI, SYBLACK],
							46: [SYBUS, SYUNDERGROUND, SYBLACK],
							58: [SYBUS, SYBLACK]}
		gameBoard[2] = 		{20: [SYTAXI, SYBLACK],
							10: [SYTAXI, SYBLACK]}
		gameBoard[3] = 		{4: [SYTAXI, SYBLACK],
							11: [SYTAXI, SYBLACK],
							12: [SYTAXI, SYBLACK],
							23: [SYBUS, SYBLACK],
							22: [SYBUS, SYBLACK]}
		gameBoard[4] = 		{3: [SYTAXI, SYBLACK],
							13: [SYTAXI, SYBLACK]}
		gameBoard[5] = 		{15: [SYTAXI, SYBLACK],
							16: [SYTAXI, SYBLACK]}
		gameBoard[6] = 		{7: [SYTAXI, SYBLACK],
							29: [SYTAXI, SYBLACK]}
		gameBoard[7] =		{6: [SYTAXI, SYBLACK],
							17: [SYTAXI, SYBLACK],
							42: [SYBUS, SYBLACK]}
		gameBoard[8] =		{1: [SYTAXI, SYBLACK],
							19: [SYTAXI, SYBLACK],
							18: [SYTAXI, SYBLACK]}
		gameBoard[9] =		{1: [SYTAXI, SYBLACK],
							19: [SYTAXI, SYBLACK],
							20: [SYTAXI, SYBLACK]}
		gameBoard[10] =		{2: [SYTAXI, SYBLACK],
							11: [SYTAXI, SYBLACK],
							21: [SYTAXI, SYBLACK],
							34: [SYTAXI, SYBLACK]}
		gameBoard[11] =		{10: [SYTAXI, SYBLACK],
							3: [SYTAXI, SYBLACK],
							22: [SYTAXI, SYBLACK]}
		gameBoard[12] =		{3: [SYTAXI, SYBLACK],
							23: [SYTAXI, SYBLACK]}
		gameBoard[13] =		{4: [SYTAXI, SYBLACK],
							14: [SYTAXI, SYBUS, SYBLACK],
							23: [SYTAXI, SYBUS, SYBLACK],
							24: [SYTAXI, SYBLACK],
							46: [SYUNDERGROUND, SYBLACK],
							52: [SYBUS, SYBLACK],
							67: [SYUNDERGROUND, SYBLACK],
							89: [SYUNDERGROUND, SYBLACK]}
		gameBoard[14] =		{13: [SYTAXI, SYBUS, SYBLACK],
							15: [SYTAXI, SYBUS, SYBLACK],
							25: [SYTAXI, SYBLACK]}
		gameBoard[15] =		{5: [SYTAXI, SYBLACK],
							14: [SYTAXI, SYBUS, SYBLACK],
							16: [SYTAXI, SYBLACK],
							26: [SYTAXI, SYBLACK],
							28: [SYTAXI, SYBLACK],
							29: [SYBUS, SYBLACK],
							41: [SYBUS, SYBLACK]}
		gameBoard[16] =		{5: [SYTAXI, SYBLACK],
							15: [SYTAXI, SYBLACK],
							28: [SYTAXI, SYBLACK],
							29: [SYTAXI, SYBLACK]}
		gameBoard[17] =		{7: [SYTAXI, SYBLACK],
							29: [SYTAXI, SYBLACK],
							30: [SYTAXI, SYBLACK]}
		gameBoard[18] =		{8: [SYTAXI, SYBLACK],
							31: [SYTAXI, SYBLACK],
							43: [SYTAXI, SYBLACK]}
		gameBoard[19] =		{8: [SYTAXI, SYBLACK],
							9: [SYTAXI, SYBLACK],
							32: [SYTAXI, SYBLACK]}
		gameBoard[20] =		{2: [SYTAXI, SYBLACK],
							9: [SYTAXI, SYBLACK],
							33: [SYTAXI, SYBLACK]}
		gameBoard[21] =		{10: [SYTAXI, SYBLACK],
							33: [SYTAXI, SYBLACK]}
		gameBoard[22] =		{3: [SYBUS, SYBLACK],
							11: [SYTAXI, SYBLACK],
							23: [SYTAXI, SYBUS, SYBLACK],
							34: [SYTAXI, SYBUS, SYBLACK],
							35: [SYTAXI, SYBLACK],
							65: [SYBUS, SYBLACK]}
		gameBoard[23] =		{3: [SYBUS, SYBLACK],
							12: [SYTAXI, SYBLACK],
							13: [SYTAXI, SYBUS, SYBLACK],
							22: [SYTAXI, SYBUS, SYBLACK],
							37: [SYTAXI, SYBLACK],
							67: [SYBUS, SYBLACK]}
		gameBoard[24] =		{13: [SYTAXI, SYBLACK],
							37: [SYTAXI, SYBLACK],
							38: [SYTAXI, SYBLACK]}
		gameBoard[25] =		{14: [SYTAXI, SYBLACK],
							38: [SYTAXI, SYBLACK],
							39: [SYTAXI, SYBLACK]}
		gameBoard[26] =		{15: [SYTAXI, SYBLACK],
							27: [SYTAXI, SYBLACK],
							39: [SYTAXI, SYBLACK]}
		gameBoard[27] =		{26: [SYTAXI, SYBLACK],
							28: [SYTAXI, SYBLACK],
							40: [SYTAXI, SYBLACK]}
		gameBoard[28] =		{15: [SYTAXI, SYBLACK],
							16: [SYTAXI, SYBLACK],
							27: [SYTAXI, SYBLACK],
							41: [SYTAXI, SYBLACK]}
		gameBoard[29] =		{6: [SYTAXI, SYBLACK],
							15: [SYBUS, SYBLACK],
							16: [SYTAXI, SYBLACK],
							17: [SYTAXI, SYBLACK],
							41: [SYTAXI, SYBUS, SYBLACK],
							42: [SYTAXI, SYBUS, SYBLACK],
							55: [SYBUS, SYBLACK]}
		gameBoard[30] =		{17: [SYTAXI, SYBLACK],
							42: [SYTAXI, SYBLACK]}
		gameBoard[31] =		{18: [SYTAXI, SYBLACK],
							43: [SYTAXI, SYBLACK],
							44: [SYTAXI, SYBLACK]}
		gameBoard[32] =		{19: [SYTAXI, SYBLACK],
							33: [SYTAXI, SYBLACK],
							44: [SYTAXI, SYBLACK],
							45: [SYTAXI, SYBLACK]}
		gameBoard[33] =		{20: [SYTAXI, SYBLACK],
							21: [SYTAXI, SYBLACK],
							32: [SYTAXI, SYBLACK],
							46: [SYTAXI, SYBLACK]}
		gameBoard[34] =		{10: [SYTAXI, SYBLACK],
							22: [SYTAXI, SYBUS, SYBLACK],
							46: [SYBUS, SYBLACK],
							47: [SYTAXI, SYBLACK],
							48: [SYTAXI, SYBLACK],
							63: [SYBUS, SYBLACK]}
		gameBoard[35] =		{22: [SYTAXI, SYBLACK],
							36: [SYTAXI, SYBLACK],
							48: [SYTAXI, SYBLACK],
							65: [SYTAXI, SYBLACK]}
		gameBoard[36] =		{35: [SYTAXI, SYBLACK],
							37: [SYTAXI, SYBLACK],
							49: [SYTAXI, SYBLACK]}
		gameBoard[37] =		{23: [SYTAXI, SYBLACK],
							24: [SYTAXI, SYBLACK],
							36: [SYTAXI, SYBLACK],
							50: [SYTAXI, SYBLACK]}
		gameBoard[38] =		{24: [SYTAXI, SYBLACK],
							25: [SYTAXI, SYBLACK],
							50: [SYTAXI, SYBLACK],
							51: [SYTAXI, SYBLACK]}
		gameBoard[39] =		{25: [SYTAXI, SYBLACK],
							26: [SYTAXI, SYBLACK],
							51: [SYTAXI, SYBLACK],
							52: [SYTAXI, SYBLACK]}
		gameBoard[40] =		{27: [SYTAXI, SYBLACK],
							41: [SYTAXI, SYBLACK],
							52: [SYTAXI, SYBLACK],
							53: [SYTAXI, SYBLACK]}
		gameBoard[41] =		{15: [SYBUS, SYBLACK],
							28: [SYTAXI, SYBLACK],
							29: [SYTAXI, SYBUS, SYBLACK],
							40: [SYTAXI, SYBLACK],
							52: [SYBUS, SYBLACK],
							54: [SYTAXI, SYBLACK],
							87: [SYBUS, SYBLACK]}
		gameBoard[42] =		{7: [SYBUS, SYBLACK],
							29: [SYTAXI, SYBUS, SYBLACK],
							30: [SYTAXI, SYBLACK],
							56: [SYTAXI, SYBLACK],
							72: [SYTAXI, SYBUS, SYBLACK]}
		gameBoard[43] =		{18: [SYTAXI, SYBLACK],
							31: [SYTAXI, SYBLACK],
							57: [SYTAXI, SYBLACK]}
		gameBoard[44] =		{31: [SYTAXI, SYBLACK],
							32: [SYTAXI, SYBLACK],
							58: [SYTAXI, SYBLACK]}
		gameBoard[45] =		{32: [SYTAXI, SYBLACK],
							46: [SYTAXI, SYBLACK],
							58: [SYTAXI, SYBLACK],
							59: [SYTAXI, SYBLACK],
							60: [SYTAXI, SYBLACK]}
		gameBoard[46] =		{1: [SYBUS, SYUNDERGROUND, SYBLACK],
							13: [SYUNDERGROUND, SYBLACK],
							33: [SYTAXI, SYBLACK],
							34: [SYBUS, SYBLACK],
							45: [SYTAXI, SYBLACK],
							47: [SYTAXI, SYBLACK],
							58: [SYBUS, SYBLACK],
							61: [SYTAXI, SYBLACK],
							74: [SYUNDERGROUND, SYBLACK],
							78: [SYBUS, SYBLACK],
							79: [SYUNDERGROUND, SYBLACK]}
		gameBoard[47] =		{34: [SYTAXI, SYBLACK],
							46: [SYTAXI, SYBLACK],
							62: [SYTAXI, SYBLACK]}
		gameBoard[48] =		{34: [SYTAXI, SYBLACK],
							35: [SYTAXI, SYBLACK],
							62: [SYTAXI, SYBLACK],
							63: [SYTAXI, SYBLACK]}
		gameBoard[49] =		{36: [SYTAXI, SYBLACK],
							50: [SYTAXI, SYBLACK],
							66: [SYTAXI, SYBLACK]}
		gameBoard[50] =		{37: [SYTAXI, SYBLACK],
							38: [SYTAXI, SYBLACK],
							49: [SYTAXI, SYBLACK]}
		gameBoard[51] =		{38: [SYTAXI, SYBLACK],
							39: [SYTAXI, SYBLACK],
							52: [SYTAXI, SYBLACK],
							67: [SYTAXI, SYBLACK],
							68: [SYTAXI, SYBLACK]}
		gameBoard[52] =		{13: [SYBUS, SYBLACK],
							39: [SYTAXI, SYBLACK],
							40: [SYTAXI, SYBLACK],
							41: [SYBUS, SYBLACK],
							51: [SYTAXI, SYBLACK],
							67: [SYBUS, SYBLACK],
							69: [SYTAXI, SYBLACK],
							86: [SYBUS, SYBLACK]}
		gameBoard[53] =		{40: [SYTAXI, SYBLACK],
							54: [SYTAXI, SYBLACK],
							69: [SYTAXI, SYBLACK]}
		gameBoard[54] =		{41: [SYTAXI, SYBLACK],
							53: [SYTAXI, SYBLACK],
							55: [SYTAXI, SYBLACK],
							70: [SYTAXI, SYBLACK]}
		gameBoard[55] =		{29: [SYBUS, SYBLACK],
							54: [SYTAXI, SYBLACK],
							71: [SYTAXI, SYBLACK],
							89: [SYBUS, SYBLACK]}
		gameBoard[56] =		{42: [SYTAXI, SYBLACK],
							91: [SYTAXI, SYBLACK]}
		gameBoard[57] =		{43: [SYTAXI, SYBLACK],
							58: [SYTAXI, SYBLACK],
							73: [SYTAXI, SYBLACK]}
		gameBoard[58] =		{1: [SYBUS, SYBLACK],
							44: [SYTAXI, SYBLACK],
							45: [SYTAXI, SYBLACK],
							46: [SYBUS, SYBLACK],
							57: [SYTAXI, SYBLACK],
							59: [SYTAXI, SYBLACK],
							74: [SYTAXI, SYBUS, SYBLACK],
							75: [SYTAXI, SYBLACK],
							77: [SYBUS, SYBLACK]}
		gameBoard[59] =		{45: [SYTAXI, SYBLACK],
							58: [SYTAXI, SYBLACK],
							75: [SYTAXI, SYBLACK],
							76: [SYTAXI, SYBLACK]}
		gameBoard[60] =		{45: [SYTAXI, SYBLACK],
							61: [SYTAXI, SYBLACK],
							76: [SYTAXI, SYBLACK]}
		gameBoard[61] =		{46: [SYTAXI, SYBLACK],
							60: [SYTAXI, SYBLACK],
							62: [SYTAXI, SYBLACK],
							76: [SYTAXI, SYBLACK],
							78: [SYTAXI, SYBLACK]}
		gameBoard[62] =		{47: [SYTAXI, SYBLACK],
							48: [SYTAXI, SYBLACK],
							61: [SYTAXI, SYBLACK],
							79: [SYTAXI, SYBLACK]}
		gameBoard[63] =		{34: [SYBUS, SYBLACK],
							48: [SYTAXI, SYBLACK],
							64: [SYTAXI, SYBLACK],
							65: [SYBUS, SYBLACK],
							79: [SYTAXI, SYBUS, SYBLACK],
							80: [SYTAXI, SYBLACK],
							100: [SYBUS, SYBLACK]}
		gameBoard[64] =		{63: [SYTAXI, SYBLACK],
							65: [SYTAXI, SYBLACK],
							81: [SYTAXI, SYBLACK]}
		gameBoard[65] =		{22: [SYBUS, SYBLACK],
							35: [SYTAXI, SYBLACK],
							63: [SYBUS, SYBLACK],
							64: [SYTAXI, SYBLACK],
							66: [SYTAXI, SYBLACK],
							67: [SYBUS, SYBLACK],
							82: [SYTAXI, SYBUS, SYBLACK]}
		gameBoard[66] =		{49: [SYTAXI, SYBLACK],
							65: [SYTAXI, SYBLACK],
							67: [SYTAXI, SYBLACK],
							82: [SYTAXI, SYBLACK]}
		gameBoard[66] =		{49: [SYTAXI, SYBLACK],
							65: [SYTAXI, SYBLACK],
							67: [SYTAXI, SYBLACK],
							82: [SYTAXI, SYBLACK]}
		gameBoard[67] =		{13: [SYUNDERGROUND, SYBLACK],
							23: [SYBUS, SYBLACK],
							51: [SYTAXI, SYBLACK],
							52: [SYBUS, SYBLACK],
							65: [SYBUS, SYBLACK],
							66: [SYTAXI, SYBLACK],
							68: [SYTAXI, SYBLACK],
							79: [SYUNDERGROUND, SYBLACK],
							82: [SYBUS, SYBLACK],
							84: [SYTAXI, SYBLACK],
							89: [SYUNDERGROUND, SYBLACK],
							102: [SYBUS, SYBLACK],
							111: [SYUNDERGROUND, SYBLACK]}
		gameBoard[68] =		{51: [SYTAXI, SYBLACK],
							67: [SYTAXI, SYBLACK],
							69: [SYTAXI, SYBLACK],
							85: [SYTAXI, SYBLACK]}
		gameBoard[69] =		{52: [SYTAXI, SYBLACK],
							53: [SYTAXI, SYBLACK],
							68: [SYTAXI, SYBLACK],
							86: [SYTAXI, SYBLACK]}
		gameBoard[70] =		{54: [SYTAXI, SYBLACK],
							71: [SYTAXI, SYBLACK],
							87: [SYTAXI, SYBLACK]}
		gameBoard[71] =		{55: [SYTAXI, SYBLACK],
							70: [SYTAXI, SYBLACK],
							72: [SYTAXI, SYBLACK],
							89: [SYTAXI, SYBLACK]}
		gameBoard[72] =		{42: [SYTAXI, SYBUS, SYBLACK],
							71: [SYTAXI, SYBLACK],
							90: [SYTAXI, SYBLACK],
							91: [SYTAXI, SYBLACK],
							105: [SYBUS, SYBLACK],
							107: [SYBUS, SYBLACK]}
		gameBoard[73] =		{57: [SYTAXI, SYBLACK],
							74: [SYTAXI, SYBLACK],
							92: [SYTAXI, SYBLACK]}
		gameBoard[74] =		{46: [SYUNDERGROUND, SYBLACK],
							58: [SYTAXI, SYBUS, SYBLACK],
							73: [SYTAXI, SYBLACK],
							75: [SYTAXI, SYBLACK],
							92: [SYTAXI, SYBLACK],
							94: [SYBUS, SYBLACK]}
		gameBoard[75] =		{58: [SYTAXI, SYBLACK],
							59: [SYTAXI, SYBLACK],
							74: [SYTAXI, SYBLACK],
							94: [SYTAXI, SYBLACK]}
		gameBoard[76] =		{59: [SYTAXI, SYBLACK],
							60: [SYTAXI, SYBLACK],
							61: [SYTAXI, SYBLACK],
							77: [SYTAXI, SYBLACK]}
		gameBoard[77] =		{58: [SYBUS, SYBLACK],
							76: [SYTAXI, SYBLACK],
							78: [SYTAXI, SYBUS, SYBLACK],
							94: [SYBUS, SYBLACK],
							95: [SYTAXI, SYBLACK],
							96: [SYTAXI, SYBLACK],
							124: [SYBUS, SYBLACK]}
		gameBoard[78] =		{46: [SYBUS, SYBLACK],
							61: [SYTAXI, SYBLACK],
							77: [SYTAXI, SYBUS, SYBLACK],
							79: [SYTAXI, SYBUS, SYBLACK],
							97: [SYTAXI, SYBLACK]}
		gameBoard[79] =		{46: [SYUNDERGROUND, SYBLACK],
							62: [SYTAXI, SYBLACK],
							63: [SYTAXI, SYBUS, SYBLACK],
							67: [SYUNDERGROUND, SYBLACK],
							78: [SYTAXI, SYBUS, SYBLACK],
							93: [SYUNDERGROUND, SYBLACK],
							98: [SYTAXI, SYBLACK],
							111: [SYUNDERGROUND, SYBLACK]}
		gameBoard[80] =		{63: [SYTAXI, SYBLACK],
							99: [SYTAXI, SYBLACK],
							100: [SYTAXI, SYBLACK]}
		gameBoard[81] =		{64: [SYTAXI, SYBLACK],
							82: [SYTAXI, SYBLACK],
							100: [SYTAXI, SYBLACK]}
		gameBoard[82] =		{65: [SYTAXI, SYBUS, SYBLACK],
							66: [SYTAXI, SYBLACK],
							67: [SYBUS, SYBLACK],
							81: [SYTAXI, SYBLACK],
							100: [SYBUS, SYBLACK],
							101: [SYTAXI, SYBLACK],
							140: [SYBUS, SYBLACK]}
		gameBoard[83] =		{101: [SYTAXI, SYBLACK],
							102: [SYTAXI, SYBLACK]}
		gameBoard[84] =		{67: [SYTAXI, SYBLACK],
							85: [SYTAXI, SYBLACK]}
		gameBoard[85] =		{68: [SYTAXI, SYBLACK],
							84: [SYTAXI, SYBLACK],
							103: [SYTAXI, SYBLACK]}
		gameBoard[86] =		{52: [SYBUS, SYBLACK],
							69: [SYTAXI, SYBLACK],
							87: [SYBUS, SYBLACK],
							102: [SYBUS, SYBLACK],
							103: [SYTAXI, SYBLACK],
							104: [SYTAXI, SYBLACK],
							116: [SYBUS, SYBLACK]}
		gameBoard[87] =		{41: [SYBUS, SYBLACK],
							70: [SYTAXI, SYBLACK],
							86: [SYBUS, SYBLACK],
							88: [SYTAXI, SYBLACK],
							105: [SYBUS, SYBLACK]}
		gameBoard[88] =		{87: [SYTAXI, SYBLACK],
							89: [SYTAXI, SYBLACK],
							117: [SYTAXI, SYBLACK]}
		gameBoard[89] =		{13: [SYUNDERGROUND, SYBLACK],
							55: [SYBUS, SYBLACK],
							67: [SYUNDERGROUND, SYBLACK],
							71: [SYTAXI, SYBLACK],
							88: [SYTAXI, SYBLACK],
							105: [SYTAXI, SYBUS, SYBLACK],
							140: [SYUNDERGROUND, SYBLACK],
							159: [SYUNDERGROUND, SYBLACK]}
		gameBoard[90] =		{72: [SYTAXI, SYBLACK],
							91: [SYTAXI, SYBLACK],
							105: [SYTAXI, SYBLACK]}
		gameBoard[91] =		{56: [SYTAXI, SYBLACK],
							72: [SYTAXI, SYBLACK],
							90: [SYTAXI, SYBLACK],
							105: [SYTAXI, SYBLACK],
							107: [SYTAXI, SYBLACK]}
		gameBoard[92] =		{73: [SYTAXI, SYBLACK],
							74: [SYTAXI, SYBLACK],
							93: [SYTAXI, SYBLACK]}
		gameBoard[93] =		{79: [SYUNDERGROUND, SYBLACK],
							92: [SYTAXI, SYBLACK],
							94: [SYTAXI, SYBUS, SYBLACK]}
		gameBoard[94] =		{74: [SYBUS, SYBLACK],
							75: [SYTAXI, SYBLACK],
							77: [SYBUS, SYBLACK],
							93: [SYTAXI, SYBUS, SYBLACK],
							95: [SYTAXI, SYBLACK]}
		gameBoard[95] =		{77: [SYTAXI, SYBLACK],
							94: [SYTAXI, SYBLACK],
							122: [SYTAXI, SYBLACK]}
		gameBoard[96] =		{77: [SYTAXI, SYBLACK],
							97: [SYTAXI, SYBLACK],
							109: [SYTAXI, SYBLACK]}
		gameBoard[97] =		{78: [SYTAXI, SYBLACK],
							96: [SYTAXI, SYBLACK],
							98: [SYTAXI, SYBLACK],
							109: [SYTAXI, SYBLACK]}
		gameBoard[98] =		{79: [SYTAXI, SYBLACK],
							97: [SYTAXI, SYBLACK],
							99: [SYTAXI, SYBLACK],
							110: [SYTAXI, SYBLACK]}
		gameBoard[99] =		{80: [SYTAXI, SYBLACK],
							98: [SYTAXI, SYBLACK],
							110: [SYTAXI, SYBLACK],
							112: [SYTAXI, SYBLACK]}
		gameBoard[100] =	{63: [SYBUS, SYBLACK],
							80: [SYTAXI, SYBLACK],
							81: [SYTAXI, SYBLACK],
							82: [SYBUS, SYBLACK],
							101: [SYTAXI, SYBLACK],
							111: [SYBUS, SYBLACK],
							112: [SYTAXI, SYBLACK],
							113: [SYTAXI, SYBLACK]}
		gameBoard[101] =	{82: [SYTAXI, SYBLACK],
							83: [SYTAXI, SYBLACK],
							100: [SYTAXI, SYBLACK],
							114: [SYTAXI, SYBLACK]}
		gameBoard[102] =	{67: [SYBUS, SYBLACK],
							83: [SYTAXI, SYBLACK],
							86: [SYBUS, SYBLACK],
							103: [SYTAXI, SYBLACK],
							115: [SYTAXI, SYBLACK],
							127: [SYBUS, SYBLACK]}
		gameBoard[103] =	{85: [SYTAXI, SYBLACK],
							86: [SYTAXI, SYBLACK],
							102: [SYTAXI, SYBLACK]}
		gameBoard[104] =	{86: [SYTAXI, SYBLACK],
							116: [SYTAXI, SYBLACK]}
		gameBoard[105] =	{72: [SYBUS, SYBLACK],
							87: [SYBUS, SYBLACK],
							89: [SYTAXI, SYBUS, SYBLACK],
							90: [SYTAXI, SYBLACK],
							91: [SYTAXI, SYBLACK],
							106: [SYTAXI, SYBLACK],
							107: [SYBUS, SYBLACK],
							118: [SYTAXI, SYBUS, SYBLACK]}
		gameBoard[106] =	{105: [SYTAXI, SYBLACK],
							107: [SYTAXI, SYBLACK]}
		gameBoard[107] =	{72: [SYBUS, SYBLACK],
							91: [SYTAXI, SYBLACK],
							105: [SYBUS, SYBLACK],
							106: [SYTAXI, SYBLACK],
							119: [SYTAXI, SYBLACK],
							161: [SYBUS, SYBLACK]}
		gameBoard[109] =	{96: [SYTAXI, SYBLACK],
							97: [SYTAXI, SYBLACK],
							110: [SYTAXI, SYBLACK],
							124: [SYTAXI, SYBLACK]}
		gameBoard[110] =	{98: [SYTAXI, SYBLACK],
							99: [SYTAXI, SYBLACK],
							109: [SYTAXI, SYBLACK],
							111: [SYTAXI, SYBLACK]}
		gameBoard[111] =	{67: [SYUNDERGROUND, SYBLACK],
							79: [SYUNDERGROUND, SYBLACK],
							100: [SYBUS, SYBLACK],
							110: [SYTAXI, SYBLACK],
							112: [SYTAXI, SYBLACK],
							124: [SYTAXI, SYBUS, SYBLACK],
							153: [SYUNDERGROUND, SYBLACK],
							163: [SYUNDERGROUND, SYBLACK]}
		gameBoard[112] =	{99: [SYTAXI, SYBLACK],
							100: [SYTAXI, SYBLACK],
							111: [SYTAXI, SYBLACK],
							125: [SYTAXI, SYBLACK]}
		gameBoard[113] =	{100: [SYTAXI, SYBLACK],
							114: [SYTAXI, SYBLACK],
							125: [SYTAXI, SYBLACK]}
		gameBoard[114] =	{101: [SYTAXI, SYBLACK],
							113: [SYTAXI, SYBLACK],
							115: [SYTAXI, SYBLACK],
							126: [SYTAXI, SYBLACK],
							131: [SYTAXI, SYBLACK],
							132: [SYTAXI, SYBLACK]}
		gameBoard[115] =	{102: [SYTAXI, SYBLACK],
							114: [SYTAXI, SYBLACK],
							118: [SYBLACK],
							126: [SYTAXI, SYBLACK],
							127: [SYTAXI, SYBLACK],
							157: [SYBLACK]}
		gameBoard[116] =	{86: [SYBUS, SYBLACK],
							104: [SYTAXI, SYBLACK],
							117: [SYTAXI, SYBLACK],
							118: [SYBUS, SYBLACK],
							127: [SYTAXI, SYBUS, SYBLACK],
							128: [SYTAXI, SYBLACK],
							142: [SYBUS, SYBLACK]}
		gameBoard[117] =	{88: [SYTAXI, SYBLACK],
							116: [SYTAXI, SYBLACK],
							118: [SYTAXI, SYBLACK],
							129: [SYTAXI, SYBLACK]}
		gameBoard[118] =	{105: [SYTAXI, SYBUS, SYBLACK],
							115: [SYBLACK],
							116: [SYBUS, SYBLACK],
							117: [SYTAXI, SYBLACK],
							119: [SYTAXI, SYBLACK],
							135: [SYBUS, SYBLACK]}
		gameBoard[119] =	{107: [SYTAXI, SYBLACK],
							118: [SYTAXI, SYBLACK],
							136: [SYTAXI, SYBLACK]}
		gameBoard[120] =	{121: [SYTAXI, SYBLACK],
							144: [SYTAXI, SYBLACK]}
		gameBoard[121] =	{120: [SYTAXI, SYBLACK],
							122: [SYTAXI, SYBLACK],
							145: [SYTAXI, SYBLACK]}
		gameBoard[122] =	{95: [SYTAXI, SYBLACK],
							121: [SYTAXI, SYBLACK],
							123: [SYTAXI, SYBUS, SYBLACK],
							144: [SYBUS, SYBUS, SYBLACK],
							146: [SYTAXI, SYBLACK]}
		gameBoard[123] =	{122: [SYTAXI, SYBUS, SYBLACK],
							124: [SYTAXI, SYBUS, SYBLACK],
							137: [SYTAXI, SYBLACK],
							144: [SYBUS, SYBLACK],
							148: [SYTAXI, SYBLACK],
							149: [SYTAXI, SYBLACK],
							165: [SYBUS, SYBLACK]}
		gameBoard[124] =	{77: [SYBUS, SYBLACK],
							109: [SYTAXI, SYBLACK],
							111: [SYTAXI, SYBUS, SYBLACK],
							123: [SYTAXI, SYBUS, SYBLACK],
							130: [SYTAXI, SYBLACK],
							138: [SYTAXI, SYBLACK],
							153: [SYBUS, SYBLACK]}
		gameBoard[125] =	{112: [SYTAXI, SYBLACK],
							113: [SYTAXI, SYBLACK],
							131: [SYTAXI, SYBLACK]}
		gameBoard[126] =	{114: [SYTAXI, SYBLACK],
							115: [SYTAXI, SYBLACK],
							127: [SYTAXI, SYBLACK],
							140: [SYTAXI, SYBLACK]}
		gameBoard[127] =	{102: [SYBUS, SYBLACK],
							115: [SYTAXI, SYBLACK],
							116: [SYTAXI, SYBUS, SYBLACK],
							126: [SYTAXI, SYBLACK],
							133: [SYTAXI, SYBUS, SYBLACK],
							134: [SYTAXI, SYBLACK]}
		gameBoard[128] =	{116: [SYTAXI, SYBLACK],
							129: [SYTAXI, SYBLACK],
							134: [SYTAXI, SYBLACK],
							142: [SYTAXI, SYBLACK]}
		gameBoard[129] =	{117: [SYTAXI, SYBLACK],
							128: [SYTAXI, SYBLACK],
							135: [SYTAXI, SYBLACK],
							142: [SYTAXI, SYBLACK],
							143: [SYTAXI, SYBLACK]}
		gameBoard[130] =	{124: [SYTAXI, SYBLACK],
							131: [SYTAXI, SYBLACK],
							139: [SYTAXI, SYBLACK]}
		gameBoard[131] =	{114: [SYTAXI, SYBLACK],
							125: [SYTAXI, SYBLACK],
							130: [SYTAXI, SYBLACK]}
		gameBoard[132] =	{114: [SYTAXI, SYBLACK],
							140: [SYTAXI, SYBLACK]}
		gameBoard[133] =	{127: [SYTAXI, SYBUS, SYBLACK],
							140: [SYTAXI, SYBUS, SYBLACK],
							141: [SYTAXI, SYBLACK],
							157: [SYBUS, SYBLACK]}
		gameBoard[134] =	{127: [SYTAXI, SYBLACK],
							128: [SYTAXI, SYBLACK],
							141: [SYTAXI, SYBLACK],
							142: [SYTAXI, SYBLACK]}
		gameBoard[135] =	{118: [SYBUS, SYBLACK],
							129: [SYTAXI, SYBLACK],
							136: [SYTAXI, SYBLACK],
							143: [SYTAXI, SYBLACK],
							159: [SYBUS, SYBLACK],
							161: [SYTAXI, SYBUS, SYBLACK]}
		gameBoard[136] =	{119: [SYTAXI, SYBLACK],
							135: [SYTAXI, SYBLACK],
							162: [SYTAXI, SYBLACK]}
		gameBoard[137] =	{123: [SYTAXI, SYBLACK],
							147: [SYTAXI, SYBLACK]}
		gameBoard[138] =	{124: [SYTAXI, SYBLACK],
							150: [SYTAXI, SYBLACK],
							152: [SYTAXI, SYBLACK]}
		gameBoard[139] =	{130: [SYTAXI, SYBLACK],
							140: [SYTAXI, SYBLACK],
							153: [SYTAXI, SYBLACK],
							154: [SYTAXI, SYBLACK]}
		gameBoard[140] =	{82: [SYBUS, SYBLACK],
							89: [SYUNDERGROUND, SYBLACK],
							126: [SYTAXI, SYBLACK],
							132: [SYTAXI, SYBLACK],
							133: [SYTAXI, SYBUS, SYBLACK],
							139: [SYTAXI, SYBLACK],
							153: [SYUNDERGROUND, SYBLACK],
							154: [SYTAXI, SYBUS, SYBLACK],
							156: [SYTAXI, SYBUS, SYBLACK],
							159: [SYUNDERGROUND, SYBLACK]}
		gameBoard[141] =	{133: [SYTAXI, SYBLACK],
							134: [SYTAXI, SYBLACK],
							142: [SYTAXI, SYBLACK],
							158: [SYTAXI, SYBLACK]}
		gameBoard[142] =	{116: [SYBUS, SYBLACK],
							128: [SYTAXI, SYBLACK],
							129: [SYTAXI, SYBLACK],
							134: [SYTAXI, SYBLACK],
							141: [SYTAXI, SYBLACK],
							143: [SYTAXI, SYBLACK],
							157: [SYBUS, SYBLACK],
							158: [SYTAXI, SYBLACK],
							159: [SYTAXI, SYBUS, SYBLACK]}
		gameBoard[143] =	{129: [SYTAXI, SYBLACK],
							135: [SYTAXI, SYBLACK],
							142: [SYTAXI, SYBLACK],
							159: [SYTAXI, SYBLACK],
							160: [SYTAXI, SYBLACK]}
		gameBoard[144] =	{120: [SYTAXI, SYBLACK],
							122: [SYBUS, SYBLACK],
							123: [SYBUS, SYBLACK],
							145: [SYTAXI, SYBLACK],
							163: [SYBUS, SYBLACK],
							177: [SYTAXI, SYBLACK]}
		gameBoard[145] =	{121: [SYTAXI, SYBLACK],
							144: [SYTAXI, SYBLACK],
							146: [SYTAXI, SYBLACK]}
		gameBoard[146] =	{122: [SYTAXI, SYBLACK],
							145: [SYTAXI, SYBLACK],
							147: [SYTAXI, SYBLACK],
							163: [SYTAXI, SYBLACK]}
		gameBoard[147] =	{137: [SYTAXI, SYBLACK],
							146: [SYTAXI, SYBLACK],
							164: [SYTAXI, SYBLACK]}
		gameBoard[148] =	{123: [SYTAXI, SYBLACK],
							149: [SYTAXI, SYBLACK],
							164: [SYTAXI, SYBLACK]}
		gameBoard[149] =	{123: [SYTAXI, SYBLACK],
							148: [SYTAXI, SYBLACK],
							150: [SYTAXI, SYBLACK],
							165: [SYTAXI, SYBLACK]}
		gameBoard[150] =	{138: [SYTAXI, SYBLACK],
							149: [SYTAXI, SYBLACK],
							151: [SYTAXI, SYBLACK]}
		gameBoard[151] =	{150: [SYTAXI, SYBLACK],
							152: [SYTAXI, SYBLACK],
							165: [SYTAXI, SYBLACK],
							166: [SYTAXI, SYBLACK]}
		gameBoard[152] =	{138: [SYTAXI, SYBLACK],
							151: [SYTAXI, SYBLACK],
							153: [SYTAXI, SYBLACK]}
		gameBoard[153] =	{111: [SYUNDERGROUND, SYBLACK],
							124: [SYBUS, SYBLACK],
							139: [SYTAXI, SYBLACK],
							140: [SYUNDERGROUND, SYBLACK],
							152: [SYTAXI, SYBLACK],
							154: [SYTAXI, SYBUS, SYBLACK],
							163: [SYUNDERGROUND, SYBLACK],
							166: [SYTAXI, SYBLACK],
							167: [SYTAXI, SYBLACK],
							180: [SYBUS, SYBLACK],
							184: [SYBUS, SYBLACK],
							185: [SYUNDERGROUND, SYBLACK]}
		gameBoard[154] =	{139: [SYTAXI, SYBLACK],
							140: [SYTAXI, SYBUS, SYBLACK],
							153: [SYTAXI, SYBUS, SYBLACK],
							155: [SYTAXI, SYBLACK],
							156: [SYBUS, SYBLACK]}
		gameBoard[155] =	{154: [SYTAXI, SYBLACK],
							156: [SYTAXI, SYBLACK],
							167: [SYTAXI, SYBLACK],
							168: [SYTAXI, SYBLACK]}
		gameBoard[156] =	{140: [SYTAXI, SYBUS, SYBLACK],
							154: [SYBUS, SYBLACK],
							155: [SYTAXI, SYBLACK],
							157: [SYTAXI, SYBUS, SYBLACK],
							169: [SYTAXI, SYBLACK],
							184: [SYBUS, SYBLACK]}
		gameBoard[157] =	{115: [SYBLACK],
							133: [SYBUS, SYBLACK],
							142: [SYBUS, SYBLACK],
							156: [SYTAXI, SYBUS, SYBLACK],
							158: [SYTAXI, SYBLACK],
							170: [SYTAXI, SYBLACK],
							185: [SYBUS, SYBLACK],
							194: [SYBLACK]}
		gameBoard[158] =	{141: [SYTAXI, SYBLACK],
							142: [SYTAXI, SYBLACK],
							157: [SYTAXI, SYBLACK],
							171: [SYTAXI, SYBLACK]}
		gameBoard[159] =	{89: [SYUNDERGROUND, SYBLACK],
							135: [SYBUS, SYBLACK],
							140: [SYUNDERGROUND, SYBLACK],
							142: [SYTAXI, SYBUS, SYBLACK],
							143: [SYTAXI, SYBLACK],
							160: [SYTAXI, SYBLACK],
							161: [SYBUS, SYBLACK],
							172: [SYTAXI, SYBLACK],
							185: [SYUNDERGROUND, SYBLACK],
							187: [SYBUS, SYBLACK],
							188: [SYTAXI, SYBLACK],
							199: [SYBUS, SYBLACK]}
		gameBoard[160] =	{143: [SYTAXI, SYBLACK],
							159: [SYTAXI, SYBLACK],
							161: [SYTAXI, SYBLACK],
							173: [SYTAXI, SYBLACK]}
		gameBoard[161] =	{107: [SYBUS, SYBLACK],
							135: [SYTAXI, SYBUS, SYBLACK],
							159: [SYBUS, SYBLACK],
							160: [SYTAXI, SYBLACK],
							174: [SYTAXI, SYBLACK],
							199: [SYBUS, SYBLACK]}
		gameBoard[162] =	{136: [SYTAXI, SYBLACK],
							175: [SYTAXI, SYBLACK]}
		gameBoard[163] =	{111: [SYUNDERGROUND, SYBLACK],
							144: [SYBUS, SYBLACK],
							146: [SYTAXI, SYBLACK],
							153: [SYUNDERGROUND, SYBLACK],
							176: [SYBUS, SYBLACK],
							177: [SYTAXI, SYBLACK],
							191: [SYBUS, SYBLACK]}
		gameBoard[164] =	{147: [SYTAXI, SYBLACK],
							148: [SYTAXI, SYBLACK],
							178: [SYTAXI, SYBLACK],
							179: [SYTAXI, SYBLACK]}
		gameBoard[165] =	{123: [SYBUS, SYBLACK],
							149: [SYTAXI, SYBLACK],
							151: [SYTAXI, SYBLACK],
							179: [SYTAXI, SYBLACK],
							180: [SYTAXI, SYBUS, SYBLACK],
							191: [SYBUS, SYBLACK]}
		gameBoard[166] =	{151: [SYTAXI, SYBLACK],
							153: [SYTAXI, SYBLACK],
							181: [SYTAXI, SYBLACK],
							183: [SYTAXI, SYBLACK]}
		gameBoard[167] =	{153: [SYTAXI, SYBLACK],
							155: [SYTAXI, SYBLACK],
							168: [SYTAXI, SYBLACK],
							183: [SYTAXI, SYBLACK]}
		gameBoard[168] =	{155: [SYTAXI, SYBLACK],
							167: [SYTAXI, SYBLACK],
							184: [SYTAXI, SYBLACK]}
		gameBoard[169] =	{156: [SYTAXI, SYBLACK],
							184: [SYTAXI, SYBLACK]}
		gameBoard[170] =	{157: [SYTAXI, SYBLACK],
							171: [SYTAXI, SYBLACK],
							185: [SYTAXI, SYBLACK]}
		gameBoard[171] =	{158: [SYTAXI, SYBLACK],
							170: [SYTAXI, SYBLACK],
							172: [SYTAXI, SYBLACK],
							186: [SYTAXI, SYBLACK],
							198: [SYTAXI, SYBLACK]}
		gameBoard[172] =	{159: [SYTAXI, SYBLACK],
							171: [SYTAXI, SYBLACK],
							187: [SYTAXI, SYBLACK]}
		gameBoard[173] =	{160: [SYTAXI, SYBLACK],
							174: [SYTAXI, SYBLACK],
							188: [SYTAXI, SYBLACK],
							200: [SYTAXI, SYBLACK]}
		gameBoard[174] =	{161: [SYTAXI, SYBLACK],
							173: [SYTAXI, SYBLACK],
							175: [SYTAXI, SYBLACK]}
		gameBoard[175] =	{162: [SYTAXI, SYBLACK],
							174: [SYTAXI, SYBLACK],
							200: [SYTAXI, SYBLACK]}
		gameBoard[176] =	{163: [SYBUS, SYBLACK],
							177: [SYTAXI, SYBLACK],
							189: [SYTAXI, SYBLACK],
							190: [SYBUS, SYBLACK]}
		gameBoard[177] =	{144: [SYTAXI, SYBLACK],
							163: [SYTAXI, SYBLACK],
							176: [SYTAXI, SYBLACK]}
		gameBoard[178] =	{164: [SYTAXI, SYBLACK],
							189: [SYTAXI, SYBLACK],
							191: [SYTAXI, SYBLACK]}
		gameBoard[179] =	{164: [SYTAXI, SYBLACK],
							165: [SYTAXI, SYBLACK],
							191: [SYTAXI, SYBLACK]}
		gameBoard[180] =	{153: [SYBUS, SYBLACK],
							165: [SYTAXI, SYBUS, SYBLACK],
							181: [SYTAXI, SYBLACK],
							184: [SYBUS, SYBLACK],
							190: [SYBUS, SYBLACK],
							193: [SYTAXI, SYBLACK]}
		gameBoard[181] =	{166: [SYTAXI, SYBLACK],
							180: [SYTAXI, SYBLACK],
							182: [SYTAXI, SYBLACK],
							193: [SYTAXI, SYBLACK]}
		gameBoard[182] =	{181: [SYTAXI, SYBLACK],
							183: [SYTAXI, SYBLACK],
							195: [SYTAXI, SYBLACK]}
		gameBoard[183] =	{166: [SYTAXI, SYBLACK],
							167: [SYTAXI, SYBLACK],
							182: [SYTAXI, SYBLACK],
							196: [SYTAXI, SYBLACK]}
		gameBoard[184] =	{153: [SYBUS, SYBLACK],
							156: [SYBUS, SYBLACK],
							168: [SYTAXI, SYBLACK],
							169: [SYTAXI, SYBLACK],
							180: [SYBUS, SYBLACK],
							185: [SYTAXI, SYBUS, SYBLACK],
							196: [SYTAXI, SYBLACK],
							197: [SYTAXI, SYBLACK]}
		gameBoard[185] =	{153: [SYUNDERGROUND, SYBLACK],
							157: [SYBUS, SYBLACK],
							159: [SYUNDERGROUND, SYBLACK],
							170: [SYTAXI, SYBLACK],
							184: [SYTAXI, SYBUS, SYBLACK],
							186: [SYTAXI, SYBLACK],
							199: [SYBUS, SYBLACK]}
		gameBoard[186] =	{171: [SYTAXI, SYBLACK],
							185: [SYTAXI, SYBLACK],
							198: [SYTAXI, SYBLACK]}
		gameBoard[187] =	{159: [SYBUS, SYBLACK],
							172: [SYTAXI, SYBLACK],
							188: [SYTAXI, SYBLACK],
							198: [SYTAXI, SYBLACK],
							199: [SYBUS, SYBLACK]}
		gameBoard[188] =	{159: [SYTAXI, SYBLACK],
							173: [SYTAXI, SYBLACK],
							187: [SYTAXI, SYBLACK],
							199: [SYTAXI, SYBLACK]}
		gameBoard[189] =	{176: [SYTAXI, SYBLACK],
							178: [SYTAXI, SYBLACK],
							190: [SYTAXI, SYBLACK]}
		gameBoard[190] =	{176: [SYBUS, SYBLACK],
							180: [SYBUS, SYBLACK],
							189: [SYTAXI, SYBLACK],
							191: [SYTAXI, SYBUS, SYBLACK],
							192: [SYTAXI, SYBLACK]}
		gameBoard[191] =	{163: [SYBUS, SYBLACK],
							165: [SYBUS, SYBLACK],
							178: [SYTAXI, SYBLACK],
							179: [SYTAXI, SYBLACK],
							190: [SYTAXI, SYBUS, SYBLACK],
							192: [SYTAXI, SYBLACK]}
		gameBoard[192] =	{190: [SYTAXI, SYBLACK],
							191: [SYTAXI, SYBLACK],
							194: [SYTAXI, SYBLACK]}
		gameBoard[193] =	{180: [SYTAXI, SYBLACK],
							181: [SYTAXI, SYBLACK],
							194: [SYTAXI, SYBLACK]}
		gameBoard[194] =	{157: [SYBLACK],
							192: [SYTAXI, SYBLACK],
							193: [SYTAXI, SYBLACK],
							195: [SYTAXI, SYBLACK]}
		gameBoard[195] =	{182: [SYTAXI, SYBLACK],
							194: [SYTAXI, SYBLACK],
							197: [SYTAXI, SYBLACK]}
		gameBoard[196] =	{183: [SYTAXI, SYBLACK],
							184: [SYTAXI, SYBLACK],
							197: [SYTAXI, SYBLACK]}
		gameBoard[197] =	{184: [SYTAXI, SYBLACK],
							195: [SYTAXI, SYBLACK],
							196: [SYTAXI, SYBLACK]}
		gameBoard[198] =	{171: [SYTAXI, SYBLACK],
							186: [SYTAXI, SYBLACK],
							187: [SYTAXI, SYBLACK]}
		gameBoard[199] =	{159: [SYBUS, SYBLACK],
							161: [SYBUS, SYBLACK],
							185: [SYBUS, SYBLACK],
							187: [SYBUS, SYBLACK],
							188: [SYTAXI, SYBLACK],
							200: [SYTAXI, SYBLACK]}
		gameBoard[200] =	{173: [SYTAXI, SYBLACK],
							175: [SYTAXI, SYBLACK],
							199: [SYTAXI, SYBLACK]}
	
		return 	gameBoard