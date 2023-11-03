from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from BaseModel.
    """

    # Public class attributes
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of City"""
        super().__init__(*args, **kwargs)
