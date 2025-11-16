class Priority:
    LOW = "low"
    MEDIUM = "medium" 
    HIGH = "high"
    
    @classmethod
    def get_priorities(cls):
        return [cls.LOW, cls.MEDIUM, cls.HIGH]
