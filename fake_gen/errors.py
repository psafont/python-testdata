class TestDataError(Exception):
    pass
class MissingElementAmountValue(TestDataError):
    pass
class FactoryStartedAlready(TestDataError):
    pass
class NoSuchDatatype(TestDataError):
    pass
class InvalidFieldType(TestDataError):
    pass
class MissingRequiredFields(TestDataError):
    pass
class UnmetDependentFields(TestDataError):
    pass
class NoFactoriesProvided(TestDataError):
    pass
class InvalidDistribution(TestDataError):
    pass
