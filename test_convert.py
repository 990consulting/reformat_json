from convert import convert
from typing import Dict


def test_empty():
    original: Dict = {}
    expected: Dict = {}
    actual: Dict = convert(original)
    assert actual == expected


def test_no_change_case():
    original: Dict = {
        "record_id": "412029665_201012",
        "irs_object_id": "201113199349201766",
    }
    expected: Dict = {
        "record_id": "412029665_201012",
        "irs_object_id": "201113199349201766",
    }
    actual: Dict = convert(original)
    assert actual == expected


def test_attribute_and_text():
    original: Dict = {
        "my_element": {
            "_": "the_value",
            "@attribute1": "foo",
            "@attribute2": "bar"
        }
    }
    expected: Dict = {
        "my_element@attribute1": "foo",
        "my_element@attribute2": "bar",
        "my_element": "the_value"
    }
    actual: Dict = convert(original)
    assert actual == expected


def test_attribute_and_text_nested():
    original: Dict = {
        "outer_dict": {
            "my_element": {
                "_": "the_value",
                "@attribute1": "foo",
                "@attribute2": "bar"
            }
        }
    }
    expected: Dict = {
        "outer_dict": {
            "my_element@attribute1": "foo",
            "my_element@attribute2": "bar",
            "my_element": "the_value"
        }
    }
    actual: Dict = convert(original)
    assert actual == expected


def test_attribute_and_text_list():
    original: Dict = {
        "outer_list": [
            {
                "my_element": {
                    "_": "value_A",
                    "@attribute1": "foo_A",
                    "@attribute2": "bar_A"
                }
            },
            {
                "my_element": {
                    "_": "value_B",
                    "@attribute1": "foo_B",
                    "@attribute2": "bar_B"
                }
            }
        ]
    }
    expected: Dict = {
        "outer_list": [
            {
                "my_element@attribute1": "foo_A",
                "my_element@attribute2": "bar_A",
                "my_element": "value_A"
            },
            {
                "my_element@attribute1": "foo_B",
                "my_element@attribute2": "bar_B",
                "my_element": "value_B"
            }
        ]
    }
    actual: Dict = convert(original)
    assert expected == actual


def test_real_attribute_case():
    original: Dict = {
        "record_id": "412029665_201012",
        "irs_object_id": "201113199349201766",
        "etree": {
            "Return": {
                "@returnVersion": "2010v3.2",
            }
        }
    }
    expected: Dict = {
        "record_id": "412029665_201012",
        "irs_object_id": "201113199349201766",
        "etree": {
            "Return@returnVersion": "2010v3.2"
        }
    }
    actual: Dict = convert(original)
    assert expected == actual


def test_real_element_text_case():
    original: Dict = {
        "record_id": "412029665_201012",
        "irs_object_id": "201113199349201766",
        "etree": {
            "Return": {
                "@returnVersion": "2010v3.2",
                "ReturnHeader": {
                    "@binaryAttachmentCount": "0",
                    "Timestamp": {
                        "_": "2011-11-15T11:52:06-08:00"
                    },
                    "TaxPeriodEndDate": {
                        "_": "2010-12-31"
                    }
                }
            }
        }
    }
    expected: Dict = {
        "record_id": "412029665_201012",
        "irs_object_id": "201113199349201766",
        "etree": {
            "Return@returnVersion": "2010v3.2",
            "Return": {
                "ReturnHeader@binaryAttachmentCount": "0",
                "ReturnHeader": {
                    "Timestamp": "2011-11-15T11:52:06-08:00",
                    "TaxPeriodEndDate": "2010-12-31"
                }
            }
        }
    }
    actual: Dict = convert(original)
    assert expected == actual


def test_real_multiple_attributes_case():
    original: Dict = {
        "record_id": "412029665_201012",
        "irs_object_id": "201113199349201766",
        "etree": {
            "Return": {
                "ReturnData": {
                    "@documentCount": "4",
                    "IRS990EZ": {
                        "@documentId": "IRS990EZ",
                        "@referenceDocumentId": "IRS990ScheduleO TransfersPersonalBenefitsContr",
                        "@softwareId": "10000105",
                        "@softwareVersion": "2010v3.2",
                        "MethodOfAccountingAccrual": {
                            "_": "X"
                        }
                    }
                }
            }
        }
    }
    expected: Dict = {
        "record_id": "412029665_201012",
        "irs_object_id": "201113199349201766",
        "etree": {
            "Return": {
                "ReturnData@documentCount": "4",
                "ReturnData": {
                    "IRS990EZ@documentId": "IRS990EZ",
                    "IRS990EZ@referenceDocumentId": "IRS990ScheduleO TransfersPersonalBenefitsContr",
                    "IRS990EZ@softwareId": "10000105",
                    "IRS990EZ@softwareVersion": "2010v3.2",
                    "IRS990EZ": {
                        "MethodOfAccountingAccrual": "X"
                    }
                }
            }
        }
    }
    actual: Dict = convert(original)
    assert expected == actual


def test_real_list_case():
    original: Dict = {
        "record_id": "412029665_201012",
        "irs_object_id": "201113199349201766",
        "etree": {
            "Return": {
                "ReturnData": {
                    "@documentCount": "4",
                    "IRS990EZ": {
                        "OfficerDirectorTrusteeKeyEmpl": [
                            {
                                "PersonName": {
                                    "_": "Charles Manock"
                                },
                                "AddressUS": {
                                    "AddressLine1": {
                                        "_": "5260 N Palm Ave"
                                    },
                                    "City": {
                                        "_": "Fresno"
                                    },
                                    "State": {
                                        "_": "CA"
                                    },
                                    "ZIPCode": {
                                        "_": "93704"
                                    }
                                },
                                "Title": {
                                    "_": "Director"
                                },
                                "AvgHoursPerWkDevotedToPosition": {
                                    "_": "0"
                                },
                                "Compensation": {
                                    "_": "0"
                                }
                            },
                            {
                                "PersonName": {
                                    "_": "Hal Kissler"
                                },
                                "AddressUS": {
                                    "AddressLine1": {
                                        "_": "P O Box 9440"
                                    },
                                    "City": {
                                        "_": "Fresno"
                                    },
                                    "State": {
                                        "_": "CA"
                                    },
                                    "ZIPCode": {
                                        "_": "93792"
                                    }
                                },
                                "Title": {
                                    "_": "Director/EBoard"
                                },
                                "AvgHoursPerWkDevotedToPosition": {
                                    "_": "1.00"
                                },
                                "Compensation": {
                                    "_": "0"
                                }
                            }
                        ]
                    }
                },
            }
        }
    }
    expected: Dict = {
        "record_id": "412029665_201012",
        "irs_object_id": "201113199349201766",
        "etree": {
            "Return": {
                "ReturnData": {
                    "IRS990EZ": {
                        "OfficerDirectorTrusteeKeyEmpl": [
                            {
                                "PersonName": "Charles Manock",
                                "AddressUS": {
                                    "AddressLine1": "5260 N Palm Ave",
                                    "City": "Fresno",
                                    "State": "CA",
                                    "ZIPCode": "93704"
                                },
                                "Title": "Director",
                                "AvgHoursPerWkDevotedToPosition": "0",
                                "Compensation": "0"
                            },
                            {
                                "PersonName": "Hal Kissler",
                                "AddressUS": {
                                    "AddressLine1": "P O Box 9440",
                                    "City": "Fresno",
                                    "State": "CA",
                                    "ZIPCode": "93792"
                                },
                                "Title": "Director/EBoard",
                                "AvgHoursPerWkDevotedToPosition": "1.00",
                                "Compensation": "0"
                            }
                        ]
                    }
                },
                "ReturnData@documentCount": "4"
            }
        }
    }
    actual: Dict = convert(original)
    assert expected == actual
