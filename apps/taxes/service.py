import uuid
from http import HTTPStatus

from ninja.errors import HttpError

from apps.taxes.models import Tax
from apps.taxes.schema import TaxCreateSchema, TaxUpdateSchema


class TaxesService:
    MAX_ENTRIES = 10

    @staticmethod
    def get_tax_by_id(tax_id: uuid.UUID):
        return Tax.objects.filter(pk=tax_id).first()

    @staticmethod
    def list_taxes():
        taxes = Tax.objects.all()
        total = taxes.count()
        return {total: total, taxes: taxes}

    def get_tax(self, tax_id: uuid.UUID):
        if not (tax := self.get_tax_by_id(tax_id)):
            raise HttpError(HTTPStatus.NOT_FOUND, "Imposto não encontrado")

        return tax

    def create_tax(self, payload: TaxCreateSchema):
        if Tax.objects.count() >= self.MAX_ENTRIES:
            raise HttpError(
                HTTPStatus.BAD_REQUEST,
                f"O limite de {self.MAX_ENTRIES} impostos foi atingido.",
            )

        return Tax.objects.create(**payload.dict())

    def update_tax(self, tax_id: uuid.UUID, payload: TaxUpdateSchema):
        if not (tax := self.get_tax_by_id(tax_id)):
            raise HttpError(HTTPStatus.NOT_FOUND, "Imposto não encontrado")

        for attr, value in payload.model_dump(
            exclude_defaults=True, exclude_unset=True
        ).items():
            setattr(tax, attr, value)

        tax.save()
        return tax