s = """At eight o'clock on Thursday morning Arthur didn't feel very good.  At nine o'clock he strted to feel better."""
def word_freq(text):
	dFreq={}
	for word in text.split():
		if word in dFreq:
			    dFreq[word] += 1
		else:
			    dFreq[word]=1
	return dFreq
    
if __name__ == "__main__":
	    import pprint
	    pprint.pprint(word_freq(s))

