from voluptuous.schema_builder import Schema, Required
from voluptuous.validators import Length, All, MultipleInvalid

class validator:
	idSchema = Schema(All(str, Length(min=24, max=24)))
	jsStrSchema=Schema(str)
	jsIntSchema=Schema(int)

	@classmethod
	def validateId(cls,sid):
		return cls.idSchema(sid)

	@classmethod
	def validateData(cls,data):
		cls.idSchema(sid)
		cls.jsStrSchema(data["title"])
		cls.jsIntSchema(data["price"])
		cls.jsIntSchema(data["inventory_count"])
		return
