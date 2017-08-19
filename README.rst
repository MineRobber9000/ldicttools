===
dictionary - Interface with system dictionary files
===

This is a GNU/Linux only library that uses dictionary files in "/usr/share/dict" to allow searching dictionaries.

For example, to get all nouns that start with the letter a in /usr/share/dict/american_english_small::

	def a_nouns():
		en_us_small = dictionary.getDict("american_english_small")
		while not en_us_small.isFinished():
			time.sleep(1)
		en_us_small = en_us_small.getObject()
		for i in en_us_small.wordType('noun',[[dictionary.STARTS_WITH,'a']]):
			yield i

To get a dictionary, call `dictionary.getDict(file: string)` where `file` is a file in /usr/share/dict. You will recieve a DictionaryThread object.
