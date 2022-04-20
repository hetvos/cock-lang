from cocksize import enum

from classes import Token

TOK = enum(
	"WORD",
	"INT",
	"STR",
	"BOOL",
)

def find_col(text,start,check):
	while start < len(text) and not check(text[start]):
		start += 1
	return start

def lex_line(line):
	col = find_col(line, 0, lambda x: not x.isspace())
	while col < len(line):
		if line[col] == '"':
			col_end = find_col(line, col+1, lambda x: x == '"')
			word = line[col+1:col_end]
			yield (col, TOK.STR, bytes(word,"utf-8").decode("unicode_escape"))
			col = find_col(line, col_end+1, lambda x: not x.isspace())
		else:
			col_end = find_col(line, col, lambda x: x.isspace())
			word = line[col:col_end]
			try: yield (col, TOK.INT, int(word))
			except:
				if word in ["true","false"]: yield (col, TOK.BOOL, bool(word))
				else: yield (col, TOK.WORD, word)
			col = find_col(line, col_end, lambda x: not x.isspace())

def lex_file(fpath):
	with open(fpath,"r") as f:
		return [Token(loc=(fpath,line,col), type=toktype, value=value) for (line, text) in enumerate(f.readlines()) for (col, toktype, value) in lex_line(text.split("$")[0])]
