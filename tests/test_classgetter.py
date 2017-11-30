import pyconrad.autoinit


# def test_subnamespaces():
#     _ = pyconrad.ClassGetter('edu.stanford.rsl.conrad.filtering')
#     filter = _.rampfilters.SheppLoganRampFilter()
#     filtertool = _.RampFilteringTool()


def test_standfordrsl_classgetter():
    _ = pyconrad.ClassGetter()
    _.stanfordrsl.conrad.filtering.rampfilters.SheppLoganRampFilter()
    _.stanfordrsl.conrad.Foo()


def test_standfordrsl():
    pyconrad.stanfordrsl().conrad.filtering.rampfilters.SheppLoganRampFilter()


if __name__ == "__main__":
    # test_subnamespaces()
    test_standfordrsl_classgetter()
    test_standfordrsl()
