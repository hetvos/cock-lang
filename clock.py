class logger:
	def __call__(self,nam,msg):
		print(f"\u001b[1m\u001b[34;1m[{nam}]\u001b[0m",msg)
	def error(self,*args):
		if len(args) >= 2:
			args = list(args)
			nam = args.pop(0)
			print(f"\u001b[1m\u001b[31;1m[\u001b[37;1m{nam} > \u001b[31;1mERROR]\u001b[0m"," ".join(args))
		else:
			print(f"\u001b[1m\u001b[31;1m[ERROR]\u001b[0m"," ".join(args))
