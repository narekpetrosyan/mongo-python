from enum import Enum, unique
    
@unique
class QueryTypes(Enum):
    GT = '$gte'
    LT = '$lte'