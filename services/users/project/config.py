class BaseConfig:
   """ Base Configuration """
   TESTING=False
   
class DevelopmentConfig(BaseConfig):
    """ Development Configuration"""
    pass

class TestingConfig(BaseConfig):
    """  Testing configuration"""
    pass

class ProductionConfiguration(BaseConfig):
    """ Production Configuration""" 
    pass
    
    
    