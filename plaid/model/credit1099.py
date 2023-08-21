"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.419.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from plaid.exceptions import ApiAttributeError


def lazy_import():
    from plaid.model.credit1099_filer import Credit1099Filer
    from plaid.model.credit1099_payer import Credit1099Payer
    from plaid.model.credit1099_recipient import Credit1099Recipient
    from plaid.model.credit_document_metadata import CreditDocumentMetadata
    from plaid.model.form1099_type import Form1099Type
    globals()['Credit1099Filer'] = Credit1099Filer
    globals()['Credit1099Payer'] = Credit1099Payer
    globals()['Credit1099Recipient'] = Credit1099Recipient
    globals()['CreditDocumentMetadata'] = CreditDocumentMetadata
    globals()['Form1099Type'] = Form1099Type


class Credit1099(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'document_id': (str, none_type,),  # noqa: E501
            'document_metadata': (CreditDocumentMetadata,),  # noqa: E501
            'form_1099_type': (Form1099Type,),  # noqa: E501
            'recipient': (Credit1099Recipient,),  # noqa: E501
            'payer': (Credit1099Payer,),  # noqa: E501
            'filer': (Credit1099Filer,),  # noqa: E501
            'tax_year': (str, none_type,),  # noqa: E501
            'rents': (float, none_type,),  # noqa: E501
            'royalties': (float, none_type,),  # noqa: E501
            'other_income': (float, none_type,),  # noqa: E501
            'federal_income_tax_withheld': (float, none_type,),  # noqa: E501
            'fishing_boat_proceeds': (float, none_type,),  # noqa: E501
            'medical_and_healthcare_payments': (float, none_type,),  # noqa: E501
            'nonemployee_compensation': (float, none_type,),  # noqa: E501
            'substitute_payments_in_lieu_of_dividends_or_interest': (float, none_type,),  # noqa: E501
            'payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer': (str, none_type,),  # noqa: E501
            'crop_insurance_proceeds': (float, none_type,),  # noqa: E501
            'excess_golden_parachute_payments': (float, none_type,),  # noqa: E501
            'gross_proceeds_paid_to_an_attorney': (float, none_type,),  # noqa: E501
            'section_409a_deferrals': (float, none_type,),  # noqa: E501
            'section_409a_income': (float, none_type,),  # noqa: E501
            'state_tax_withheld': (float, none_type,),  # noqa: E501
            'state_tax_withheld_lower': (float, none_type,),  # noqa: E501
            'payer_state_number': (str, none_type,),  # noqa: E501
            'payer_state_number_lower': (str, none_type,),  # noqa: E501
            'state_income': (float, none_type,),  # noqa: E501
            'state_income_lower': (float, none_type,),  # noqa: E501
            'transactions_reported': (str, none_type,),  # noqa: E501
            'pse_name': (str, none_type,),  # noqa: E501
            'pse_telephone_number': (str, none_type,),  # noqa: E501
            'gross_amount': (float, none_type,),  # noqa: E501
            'card_not_present_transaction': (float, none_type,),  # noqa: E501
            'merchant_category_code': (str, none_type,),  # noqa: E501
            'number_of_payment_transactions': (str, none_type,),  # noqa: E501
            'january_amount': (float, none_type,),  # noqa: E501
            'february_amount': (float, none_type,),  # noqa: E501
            'march_amount': (float, none_type,),  # noqa: E501
            'april_amount': (float, none_type,),  # noqa: E501
            'may_amount': (float, none_type,),  # noqa: E501
            'june_amount': (float, none_type,),  # noqa: E501
            'july_amount': (float, none_type,),  # noqa: E501
            'august_amount': (float, none_type,),  # noqa: E501
            'september_amount': (float, none_type,),  # noqa: E501
            'october_amount': (float, none_type,),  # noqa: E501
            'november_amount': (float, none_type,),  # noqa: E501
            'december_amount': (float, none_type,),  # noqa: E501
            'primary_state': (str, none_type,),  # noqa: E501
            'secondary_state': (str, none_type,),  # noqa: E501
            'primary_state_id': (str, none_type,),  # noqa: E501
            'secondary_state_id': (str, none_type,),  # noqa: E501
            'primary_state_income_tax': (float, none_type,),  # noqa: E501
            'secondary_state_income_tax': (float, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'document_id': 'document_id',  # noqa: E501
        'document_metadata': 'document_metadata',  # noqa: E501
        'form_1099_type': 'form_1099_type',  # noqa: E501
        'recipient': 'recipient',  # noqa: E501
        'payer': 'payer',  # noqa: E501
        'filer': 'filer',  # noqa: E501
        'tax_year': 'tax_year',  # noqa: E501
        'rents': 'rents',  # noqa: E501
        'royalties': 'royalties',  # noqa: E501
        'other_income': 'other_income',  # noqa: E501
        'federal_income_tax_withheld': 'federal_income_tax_withheld',  # noqa: E501
        'fishing_boat_proceeds': 'fishing_boat_proceeds',  # noqa: E501
        'medical_and_healthcare_payments': 'medical_and_healthcare_payments',  # noqa: E501
        'nonemployee_compensation': 'nonemployee_compensation',  # noqa: E501
        'substitute_payments_in_lieu_of_dividends_or_interest': 'substitute_payments_in_lieu_of_dividends_or_interest',  # noqa: E501
        'payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer': 'payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer',  # noqa: E501
        'crop_insurance_proceeds': 'crop_insurance_proceeds',  # noqa: E501
        'excess_golden_parachute_payments': 'excess_golden_parachute_payments',  # noqa: E501
        'gross_proceeds_paid_to_an_attorney': 'gross_proceeds_paid_to_an_attorney',  # noqa: E501
        'section_409a_deferrals': 'section_409a_deferrals',  # noqa: E501
        'section_409a_income': 'section_409a_income',  # noqa: E501
        'state_tax_withheld': 'state_tax_withheld',  # noqa: E501
        'state_tax_withheld_lower': 'state_tax_withheld_lower',  # noqa: E501
        'payer_state_number': 'payer_state_number',  # noqa: E501
        'payer_state_number_lower': 'payer_state_number_lower',  # noqa: E501
        'state_income': 'state_income',  # noqa: E501
        'state_income_lower': 'state_income_lower',  # noqa: E501
        'transactions_reported': 'transactions_reported',  # noqa: E501
        'pse_name': 'pse_name',  # noqa: E501
        'pse_telephone_number': 'pse_telephone_number',  # noqa: E501
        'gross_amount': 'gross_amount',  # noqa: E501
        'card_not_present_transaction': 'card_not_present_transaction',  # noqa: E501
        'merchant_category_code': 'merchant_category_code',  # noqa: E501
        'number_of_payment_transactions': 'number_of_payment_transactions',  # noqa: E501
        'january_amount': 'january_amount',  # noqa: E501
        'february_amount': 'february_amount',  # noqa: E501
        'march_amount': 'march_amount',  # noqa: E501
        'april_amount': 'april_amount',  # noqa: E501
        'may_amount': 'may_amount',  # noqa: E501
        'june_amount': 'june_amount',  # noqa: E501
        'july_amount': 'july_amount',  # noqa: E501
        'august_amount': 'august_amount',  # noqa: E501
        'september_amount': 'september_amount',  # noqa: E501
        'october_amount': 'october_amount',  # noqa: E501
        'november_amount': 'november_amount',  # noqa: E501
        'december_amount': 'december_amount',  # noqa: E501
        'primary_state': 'primary_state',  # noqa: E501
        'secondary_state': 'secondary_state',  # noqa: E501
        'primary_state_id': 'primary_state_id',  # noqa: E501
        'secondary_state_id': 'secondary_state_id',  # noqa: E501
        'primary_state_income_tax': 'primary_state_income_tax',  # noqa: E501
        'secondary_state_income_tax': 'secondary_state_income_tax',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, document_id, *args, **kwargs):  # noqa: E501
        """Credit1099 - a model defined in OpenAPI

        Args:
            document_id (str, none_type): An identifier of the document referenced by the document metadata.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            document_metadata (CreditDocumentMetadata): [optional]  # noqa: E501
            form_1099_type (Form1099Type): [optional]  # noqa: E501
            recipient (Credit1099Recipient): [optional]  # noqa: E501
            payer (Credit1099Payer): [optional]  # noqa: E501
            filer (Credit1099Filer): [optional]  # noqa: E501
            tax_year (str, none_type): Tax year of the tax form.. [optional]  # noqa: E501
            rents (float, none_type): Amount in rent by payer.. [optional]  # noqa: E501
            royalties (float, none_type): Amount in royalties by payer.. [optional]  # noqa: E501
            other_income (float, none_type): Amount in other income by payer.. [optional]  # noqa: E501
            federal_income_tax_withheld (float, none_type): Amount of federal income tax withheld from payer.. [optional]  # noqa: E501
            fishing_boat_proceeds (float, none_type): Amount of fishing boat proceeds from payer.. [optional]  # noqa: E501
            medical_and_healthcare_payments (float, none_type): Amount of medical and healthcare payments from payer.. [optional]  # noqa: E501
            nonemployee_compensation (float, none_type): Amount of nonemployee compensation from payer.. [optional]  # noqa: E501
            substitute_payments_in_lieu_of_dividends_or_interest (float, none_type): Amount of substitute payments made by payer.. [optional]  # noqa: E501
            payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer (str, none_type): Whether or not payer made direct sales over $5000 of consumer products.. [optional]  # noqa: E501
            crop_insurance_proceeds (float, none_type): Amount of crop insurance proceeds.. [optional]  # noqa: E501
            excess_golden_parachute_payments (float, none_type): Amount of golden parachute payments made by payer.. [optional]  # noqa: E501
            gross_proceeds_paid_to_an_attorney (float, none_type): Amount of gross proceeds paid to an attorney by payer.. [optional]  # noqa: E501
            section_409a_deferrals (float, none_type): Amount of 409A deferrals earned by payer.. [optional]  # noqa: E501
            section_409a_income (float, none_type): Amount of 409A income earned by payer.. [optional]  # noqa: E501
            state_tax_withheld (float, none_type): Amount of state tax withheld of payer for primary state.. [optional]  # noqa: E501
            state_tax_withheld_lower (float, none_type): Amount of state tax withheld of payer for secondary state.. [optional]  # noqa: E501
            payer_state_number (str, none_type): Primary state ID.. [optional]  # noqa: E501
            payer_state_number_lower (str, none_type): Secondary state ID.. [optional]  # noqa: E501
            state_income (float, none_type): State income reported for primary state.. [optional]  # noqa: E501
            state_income_lower (float, none_type): State income reported for secondary state.. [optional]  # noqa: E501
            transactions_reported (str, none_type): One of the values will be provided Payment card Third party network. [optional]  # noqa: E501
            pse_name (str, none_type): Name of the PSE (Payment Settlement Entity).. [optional]  # noqa: E501
            pse_telephone_number (str, none_type): Formatted (XXX) XXX-XXXX. Phone number of the PSE (Payment Settlement Entity).. [optional]  # noqa: E501
            gross_amount (float, none_type): Gross amount reported.. [optional]  # noqa: E501
            card_not_present_transaction (float, none_type): Amount in card not present transactions.. [optional]  # noqa: E501
            merchant_category_code (str, none_type): Merchant category of filer.. [optional]  # noqa: E501
            number_of_payment_transactions (str, none_type): Number of payment transactions made.. [optional]  # noqa: E501
            january_amount (float, none_type): Amount reported for January.. [optional]  # noqa: E501
            february_amount (float, none_type): Amount reported for February.. [optional]  # noqa: E501
            march_amount (float, none_type): Amount reported for March.. [optional]  # noqa: E501
            april_amount (float, none_type): Amount reported for April.. [optional]  # noqa: E501
            may_amount (float, none_type): Amount reported for May.. [optional]  # noqa: E501
            june_amount (float, none_type): Amount reported for June.. [optional]  # noqa: E501
            july_amount (float, none_type): Amount reported for July.. [optional]  # noqa: E501
            august_amount (float, none_type): Amount reported for August.. [optional]  # noqa: E501
            september_amount (float, none_type): Amount reported for September.. [optional]  # noqa: E501
            october_amount (float, none_type): Amount reported for October.. [optional]  # noqa: E501
            november_amount (float, none_type): Amount reported for November.. [optional]  # noqa: E501
            december_amount (float, none_type): Amount reported for December.. [optional]  # noqa: E501
            primary_state (str, none_type): Primary state of business.. [optional]  # noqa: E501
            secondary_state (str, none_type): Secondary state of business.. [optional]  # noqa: E501
            primary_state_id (str, none_type): Primary state ID.. [optional]  # noqa: E501
            secondary_state_id (str, none_type): Secondary state ID.. [optional]  # noqa: E501
            primary_state_income_tax (float, none_type): State income tax reported for primary state.. [optional]  # noqa: E501
            secondary_state_income_tax (float, none_type): State income tax reported for secondary state.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.document_id = document_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, document_id, *args, **kwargs):  # noqa: E501
        """Credit1099 - a model defined in OpenAPI

        Args:
            document_id (str, none_type): An identifier of the document referenced by the document metadata.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            document_metadata (CreditDocumentMetadata): [optional]  # noqa: E501
            form_1099_type (Form1099Type): [optional]  # noqa: E501
            recipient (Credit1099Recipient): [optional]  # noqa: E501
            payer (Credit1099Payer): [optional]  # noqa: E501
            filer (Credit1099Filer): [optional]  # noqa: E501
            tax_year (str, none_type): Tax year of the tax form.. [optional]  # noqa: E501
            rents (float, none_type): Amount in rent by payer.. [optional]  # noqa: E501
            royalties (float, none_type): Amount in royalties by payer.. [optional]  # noqa: E501
            other_income (float, none_type): Amount in other income by payer.. [optional]  # noqa: E501
            federal_income_tax_withheld (float, none_type): Amount of federal income tax withheld from payer.. [optional]  # noqa: E501
            fishing_boat_proceeds (float, none_type): Amount of fishing boat proceeds from payer.. [optional]  # noqa: E501
            medical_and_healthcare_payments (float, none_type): Amount of medical and healthcare payments from payer.. [optional]  # noqa: E501
            nonemployee_compensation (float, none_type): Amount of nonemployee compensation from payer.. [optional]  # noqa: E501
            substitute_payments_in_lieu_of_dividends_or_interest (float, none_type): Amount of substitute payments made by payer.. [optional]  # noqa: E501
            payer_made_direct_sales_of_5000_or_more_of_consumer_products_to_buyer (str, none_type): Whether or not payer made direct sales over $5000 of consumer products.. [optional]  # noqa: E501
            crop_insurance_proceeds (float, none_type): Amount of crop insurance proceeds.. [optional]  # noqa: E501
            excess_golden_parachute_payments (float, none_type): Amount of golden parachute payments made by payer.. [optional]  # noqa: E501
            gross_proceeds_paid_to_an_attorney (float, none_type): Amount of gross proceeds paid to an attorney by payer.. [optional]  # noqa: E501
            section_409a_deferrals (float, none_type): Amount of 409A deferrals earned by payer.. [optional]  # noqa: E501
            section_409a_income (float, none_type): Amount of 409A income earned by payer.. [optional]  # noqa: E501
            state_tax_withheld (float, none_type): Amount of state tax withheld of payer for primary state.. [optional]  # noqa: E501
            state_tax_withheld_lower (float, none_type): Amount of state tax withheld of payer for secondary state.. [optional]  # noqa: E501
            payer_state_number (str, none_type): Primary state ID.. [optional]  # noqa: E501
            payer_state_number_lower (str, none_type): Secondary state ID.. [optional]  # noqa: E501
            state_income (float, none_type): State income reported for primary state.. [optional]  # noqa: E501
            state_income_lower (float, none_type): State income reported for secondary state.. [optional]  # noqa: E501
            transactions_reported (str, none_type): One of the values will be provided Payment card Third party network. [optional]  # noqa: E501
            pse_name (str, none_type): Name of the PSE (Payment Settlement Entity).. [optional]  # noqa: E501
            pse_telephone_number (str, none_type): Formatted (XXX) XXX-XXXX. Phone number of the PSE (Payment Settlement Entity).. [optional]  # noqa: E501
            gross_amount (float, none_type): Gross amount reported.. [optional]  # noqa: E501
            card_not_present_transaction (float, none_type): Amount in card not present transactions.. [optional]  # noqa: E501
            merchant_category_code (str, none_type): Merchant category of filer.. [optional]  # noqa: E501
            number_of_payment_transactions (str, none_type): Number of payment transactions made.. [optional]  # noqa: E501
            january_amount (float, none_type): Amount reported for January.. [optional]  # noqa: E501
            february_amount (float, none_type): Amount reported for February.. [optional]  # noqa: E501
            march_amount (float, none_type): Amount reported for March.. [optional]  # noqa: E501
            april_amount (float, none_type): Amount reported for April.. [optional]  # noqa: E501
            may_amount (float, none_type): Amount reported for May.. [optional]  # noqa: E501
            june_amount (float, none_type): Amount reported for June.. [optional]  # noqa: E501
            july_amount (float, none_type): Amount reported for July.. [optional]  # noqa: E501
            august_amount (float, none_type): Amount reported for August.. [optional]  # noqa: E501
            september_amount (float, none_type): Amount reported for September.. [optional]  # noqa: E501
            october_amount (float, none_type): Amount reported for October.. [optional]  # noqa: E501
            november_amount (float, none_type): Amount reported for November.. [optional]  # noqa: E501
            december_amount (float, none_type): Amount reported for December.. [optional]  # noqa: E501
            primary_state (str, none_type): Primary state of business.. [optional]  # noqa: E501
            secondary_state (str, none_type): Secondary state of business.. [optional]  # noqa: E501
            primary_state_id (str, none_type): Primary state ID.. [optional]  # noqa: E501
            secondary_state_id (str, none_type): Secondary state ID.. [optional]  # noqa: E501
            primary_state_income_tax (float, none_type): State income tax reported for primary state.. [optional]  # noqa: E501
            secondary_state_income_tax (float, none_type): State income tax reported for secondary state.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.document_id = document_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
