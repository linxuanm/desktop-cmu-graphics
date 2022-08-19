def assertError(fn, errorKeywords):
    raised = True
    try:
        fn()
        raised = False
    except Exception as e:
        msg = str(e).lower()
        for kw in errorKeywords:
          if not kw.lower() in msg:
            raise Exception(f'error message should contain {kw} but was {msg}')
    if not raised:
        raise Exception('fn failed to raise an exception')

###########
# Ensure i18n for list remove works

a = [0, 1, 2]
a.remove(0)
assert a == [1, 2]

###########
# Typechecking for images and sounds
# On Desktop, 'test' is interpreted as a relative filepath

assertError(lambda: Sound('test'), ['Sound.url', 'http://'])
assertError(lambda: Image('test', 20, 20), ['Image.url', 'http://'])

###########
# Calling class methods with too few arguments
# On Desktop, Python handles missing arguments on its own
assertError(lambda: g.hits(), ['Missing a required argument'])
assertError(lambda: g.remove(), ['Missing a required argument'])