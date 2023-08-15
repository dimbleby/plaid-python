"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.410.1
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
    from plaid.model.location import Location
    from plaid.model.payment_meta import PaymentMeta
    from plaid.model.personal_finance_category import PersonalFinanceCategory
    from plaid.model.transaction_all_of import TransactionAllOf
    from plaid.model.transaction_base import TransactionBase
    from plaid.model.transaction_code import TransactionCode
    from plaid.model.transaction_counterparty import TransactionCounterparty
    globals()['Location'] = Location
    globals()['PaymentMeta'] = PaymentMeta
    globals()['PersonalFinanceCategory'] = PersonalFinanceCategory
    globals()['TransactionAllOf'] = TransactionAllOf
    globals()['TransactionBase'] = TransactionBase
    globals()['TransactionCode'] = TransactionCode
    globals()['TransactionCounterparty'] = TransactionCounterparty


class Transaction(ModelComposed):
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
        ('payment_channel',): {
            'ONLINE': "online",
            'IN_STORE': "in store",
            'OTHER': "other",
        },
        ('transaction_type',): {
            'DIGITAL': "digital",
            'PLACE': "place",
            'SPECIAL': "special",
            'UNRESOLVED': "unresolved",
        },
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
            'account_id': (str,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'iso_currency_code': (str, none_type,),  # noqa: E501
            'unofficial_currency_code': (str, none_type,),  # noqa: E501
            'category': ([str], none_type,),  # noqa: E501
            'category_id': (str, none_type,),  # noqa: E501
            'date': (date,),  # noqa: E501
            'location': (Location,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'payment_meta': (PaymentMeta,),  # noqa: E501
            'pending': (bool,),  # noqa: E501
            'pending_transaction_id': (str, none_type,),  # noqa: E501
            'account_owner': (str, none_type,),  # noqa: E501
            'transaction_id': (str,),  # noqa: E501
            'authorized_date': (date, none_type,),  # noqa: E501
            'authorized_datetime': (datetime, none_type,),  # noqa: E501
            'datetime': (datetime, none_type,),  # noqa: E501
            'payment_channel': (str,),  # noqa: E501
            'transaction_code': (TransactionCode,),  # noqa: E501
            'check_number': (str, none_type,),  # noqa: E501
            'merchant_name': (str, none_type,),  # noqa: E501
            'original_description': (str, none_type,),  # noqa: E501
            'transaction_type': (str,),  # noqa: E501
            'logo_url': (str, none_type,),  # noqa: E501
            'website': (str, none_type,),  # noqa: E501
            'personal_finance_category': (PersonalFinanceCategory,),  # noqa: E501
            'personal_finance_category_icon_url': (str,),  # noqa: E501
            'counterparties': ([TransactionCounterparty],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'account_id': 'account_id',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'iso_currency_code': 'iso_currency_code',  # noqa: E501
        'unofficial_currency_code': 'unofficial_currency_code',  # noqa: E501
        'category': 'category',  # noqa: E501
        'category_id': 'category_id',  # noqa: E501
        'date': 'date',  # noqa: E501
        'location': 'location',  # noqa: E501
        'name': 'name',  # noqa: E501
        'payment_meta': 'payment_meta',  # noqa: E501
        'pending': 'pending',  # noqa: E501
        'pending_transaction_id': 'pending_transaction_id',  # noqa: E501
        'account_owner': 'account_owner',  # noqa: E501
        'transaction_id': 'transaction_id',  # noqa: E501
        'authorized_date': 'authorized_date',  # noqa: E501
        'authorized_datetime': 'authorized_datetime',  # noqa: E501
        'datetime': 'datetime',  # noqa: E501
        'payment_channel': 'payment_channel',  # noqa: E501
        'transaction_code': 'transaction_code',  # noqa: E501
        'check_number': 'check_number',  # noqa: E501
        'merchant_name': 'merchant_name',  # noqa: E501
        'original_description': 'original_description',  # noqa: E501
        'transaction_type': 'transaction_type',  # noqa: E501
        'logo_url': 'logo_url',  # noqa: E501
        'website': 'website',  # noqa: E501
        'personal_finance_category': 'personal_finance_category',  # noqa: E501
        'personal_finance_category_icon_url': 'personal_finance_category_icon_url',  # noqa: E501
        'counterparties': 'counterparties',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Transaction - a model defined in OpenAPI

        Keyword Args:
            account_id (str): The ID of the account in which this transaction occurred.
            amount (float): The settled value of the transaction, denominated in the transactions's currency, as stated in `iso_currency_code` or `unofficial_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative.
            iso_currency_code (str, none_type): The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-null.
            unofficial_currency_code (str, none_type): The unofficial currency code associated with the transaction. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
            category ([str], none_type): A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).  All Transactions implementations are recommended to use the new `personal_finance_category` instead of `category`. `personal_finance_category` provides more meaningful categorization and greater accuracy.  If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
            category_id (str, none_type): The ID of the category to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).  All Transactions implementations are recommended to use the new `personal_finance_category` instead of `category_id`, as it provides greater accuracy and more meaningful categorization.  If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
            date (date): For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` ). To receive information about the date that a posted transaction was initiated, see the `authorized_date` field.
            location (Location):
            name (str): The merchant name or transaction description.  If the `transactions` object was returned by a Transactions endpoint such as `/transactions/sync` or `/transactions/get`, this field will always appear. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
            payment_meta (PaymentMeta):
            pending (bool): When `true`, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled.
            pending_transaction_id (str, none_type): The ID of a posted transaction's associated pending transaction, where applicable.
            account_owner (str, none_type): The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts.
            transaction_id (str): The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive.
            authorized_date (date, none_type): The date that the transaction was authorized. For posted transactions, the `date` field will indicate the posted date, but `authorized_date` will indicate the day the transaction was authorized by the financial institution. If presenting transactions to the user in a UI, the `authorized_date`, when available, is generally preferable to use over the `date` field for posted transactions, as it will generally represent the date the user actually made the transaction. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` ).
            authorized_datetime (datetime, none_type): Date and time when a transaction was authorized in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ). For posted transactions, the `datetime` field will indicate the posted date, but `authorized_datetime` will indicate the day the transaction was authorized by the financial institution. If presenting transactions to the user in a UI, the `authorized_datetime`, when available, is generally preferable to use over the `datetime` field for posted transactions, as it will generally represent the date the user actually made the transaction.  This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00). This field is only populated in API version 2019-05-29 and later.
            datetime (datetime, none_type): Date and time when a transaction was posted in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ). For the date that the transaction was initiated, rather than posted, see the `authorized_datetime` field.  This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00). This field is only populated in API version 2019-05-29 and later.
            payment_channel (str): The channel used to make a payment. `online:` transactions that took place online.  `in store:` transactions that were made at a physical location.  `other:` transactions that relate to banks, e.g. fees or deposits.  This field replaces the `transaction_type` field. 
            transaction_code (TransactionCode):
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
            check_number (str, none_type): The check number of the transaction. This field is only populated for check transactions.. [optional]  # noqa: E501
            merchant_name (str, none_type): The merchant name, as enriched by Plaid from the `name` field. This is typically a more human-readable version of the merchant counterparty in the transaction. For some bank transactions (such as checks or account transfers) where there is no meaningful merchant name, this value will be `null`.. [optional]  # noqa: E501
            original_description (str, none_type): The string returned by the financial institution to describe the transaction. For transactions returned by `/transactions/sync` or `/transactions/get`, this field is in beta and will be omitted unless the client is both enrolled in the closed beta program and has set `options.include_original_description` to `true`.. [optional]  # noqa: E501
            transaction_type (str): Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.  `digital:` transactions that took place online.  `place:` transactions that were made at a physical location.  `special:` transactions that relate to banks, e.g. fees or deposits.  `unresolved:` transactions that do not fit into the other three types. . [optional]  # noqa: E501
            logo_url (str, none_type): The logo associated with the merchant, if available. Formatted as a 100x100 pixels PNG file path.. [optional]  # noqa: E501
            website (str, none_type): The website associated with the merchant, if available.. [optional]  # noqa: E501
            personal_finance_category (PersonalFinanceCategory): [optional]  # noqa: E501
            personal_finance_category_icon_url (str): A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels.. [optional]  # noqa: E501
            counterparties ([TransactionCounterparty]): The counterparties present in the transaction. Counterparties, such as the financial institutions, are extracted by Plaid from the raw description.. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Transaction - a model defined in OpenAPI

        Keyword Args:
            account_id (str): The ID of the account in which this transaction occurred.
            amount (float): The settled value of the transaction, denominated in the transactions's currency, as stated in `iso_currency_code` or `unofficial_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative.
            iso_currency_code (str, none_type): The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-null.
            unofficial_currency_code (str, none_type): The unofficial currency code associated with the transaction. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.
            category ([str], none_type): A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).  All Transactions implementations are recommended to use the new `personal_finance_category` instead of `category`. `personal_finance_category` provides more meaningful categorization and greater accuracy.  If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
            category_id (str, none_type): The ID of the category to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).  All Transactions implementations are recommended to use the new `personal_finance_category` instead of `category_id`, as it provides greater accuracy and more meaningful categorization.  If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
            date (date): For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` ). To receive information about the date that a posted transaction was initiated, see the `authorized_date` field.
            location (Location):
            name (str): The merchant name or transaction description.  If the `transactions` object was returned by a Transactions endpoint such as `/transactions/sync` or `/transactions/get`, this field will always appear. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.
            payment_meta (PaymentMeta):
            pending (bool): When `true`, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled.
            pending_transaction_id (str, none_type): The ID of a posted transaction's associated pending transaction, where applicable.
            account_owner (str, none_type): The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts.
            transaction_id (str): The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive.
            authorized_date (date, none_type): The date that the transaction was authorized. For posted transactions, the `date` field will indicate the posted date, but `authorized_date` will indicate the day the transaction was authorized by the financial institution. If presenting transactions to the user in a UI, the `authorized_date`, when available, is generally preferable to use over the `date` field for posted transactions, as it will generally represent the date the user actually made the transaction. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` ).
            authorized_datetime (datetime, none_type): Date and time when a transaction was authorized in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ). For posted transactions, the `datetime` field will indicate the posted date, but `authorized_datetime` will indicate the day the transaction was authorized by the financial institution. If presenting transactions to the user in a UI, the `authorized_datetime`, when available, is generally preferable to use over the `datetime` field for posted transactions, as it will generally represent the date the user actually made the transaction.  This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00). This field is only populated in API version 2019-05-29 and later.
            datetime (datetime, none_type): Date and time when a transaction was posted in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ). For the date that the transaction was initiated, rather than posted, see the `authorized_datetime` field.  This field is returned for select financial institutions and comes as provided by the institution. It may contain default time values (such as 00:00:00). This field is only populated in API version 2019-05-29 and later.
            payment_channel (str): The channel used to make a payment. `online:` transactions that took place online.  `in store:` transactions that were made at a physical location.  `other:` transactions that relate to banks, e.g. fees or deposits.  This field replaces the `transaction_type` field. 
            transaction_code (TransactionCode):
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
            check_number (str, none_type): The check number of the transaction. This field is only populated for check transactions.. [optional]  # noqa: E501
            merchant_name (str, none_type): The merchant name, as enriched by Plaid from the `name` field. This is typically a more human-readable version of the merchant counterparty in the transaction. For some bank transactions (such as checks or account transfers) where there is no meaningful merchant name, this value will be `null`.. [optional]  # noqa: E501
            original_description (str, none_type): The string returned by the financial institution to describe the transaction. For transactions returned by `/transactions/sync` or `/transactions/get`, this field is in beta and will be omitted unless the client is both enrolled in the closed beta program and has set `options.include_original_description` to `true`.. [optional]  # noqa: E501
            transaction_type (str): Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.  `digital:` transactions that took place online.  `place:` transactions that were made at a physical location.  `special:` transactions that relate to banks, e.g. fees or deposits.  `unresolved:` transactions that do not fit into the other three types. . [optional]  # noqa: E501
            logo_url (str, none_type): The logo associated with the merchant, if available. Formatted as a 100x100 pixels PNG file path.. [optional]  # noqa: E501
            website (str, none_type): The website associated with the merchant, if available.. [optional]  # noqa: E501
            personal_finance_category (PersonalFinanceCategory): [optional]  # noqa: E501
            personal_finance_category_icon_url (str): A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels.. [optional]  # noqa: E501
            counterparties ([TransactionCounterparty]): The counterparties present in the transaction. Counterparties, such as the financial institutions, are extracted by Plaid from the raw description.. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              TransactionAllOf,
              TransactionBase,
          ],
          'oneOf': [
          ],
        }
