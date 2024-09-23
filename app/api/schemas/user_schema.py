from pydantic import BaseModel, Field, field_validator
from typing import Optional


class user_schema_create(BaseModel):
    
    user_name: str = Field(max_length=50)
    password: str = Field(min_length=6, description='Password must have at least 6 characters and 1 number.')

    model_config = {'json_schema_extra':{ #Cambia el valor por defecto del esquema de ejemplo 
        'example':{
            'user_name':'user',
            'password': 'password1'
        }
    }}

    @field_validator('password') #Validaciones flexibles de parametros.
    def validate_password(cls, value):
        if not any(char.isnumeric() for char in value):
            raise ValueError('Password must have 1 number')

