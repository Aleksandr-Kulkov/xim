from pdf import pdf_to_dict


def test_keys_presence(file='test_task'):
    file_keys = pdf_to_dict(file).keys()

    assert 'PN' in file_keys
    assert 'SN' in file_keys
    assert 'DESCRIPTION' in file_keys
    assert 'LOCATION' in file_keys
    assert 'CONDITION' in file_keys
    assert 'RECEIVER#' in file_keys
    assert 'UOM' in file_keys
    assert 'EXP DATE' in file_keys
    assert 'PO' in file_keys
    assert 'CERT SOURCE' in file_keys
    assert 'REC.DATE' in file_keys
    assert 'MFG' in file_keys
    assert 'BATCH#' in file_keys
    assert 'DOM' in file_keys
    assert 'REMARK' in file_keys
    assert 'LOT#' in file_keys
    assert 'TAGGED BY' in file_keys
    assert 'Qty' in file_keys
    assert 'NOTES' in file_keys
