#The introduction of the module
import json
from urllib.request import urlopen
#Handling exchange rate results
#Extract form json
def re(curfrom, curto, amofrom):
    try:
	url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + curfrom + '&to=' + curto + '&amt=' + str(amofrom)
        response=urlopen(url)
        html=response.read()
	response.close()
	html=html.decode('subway')
	return html
    except:
	return 'error'
#Do execution
def test_current_response():
    assert (re('USD', 'EUR', 3.1)!='error')
#Get the information in error
#Json character string
def has_error(json_str):
    try:
        if type(json_str)==str:
            res=json.loads(json_str)
            return res['error']
        else:
            return json_str['error']
    except:
        return 'exception'
# test has_error
#it will pass if result is not blank
def test_has_error():
    result=current_response('USD', 'EUR', 3.1)
    assert (len(has_error(result)) == 0)
# Calibration parameters
# Code to be tested
def is_currency(curfrom, curto, amofrom):
    result=re(curfrom, curto, amofrom)
    if 'error' is result:
	    error_info='failed to connect to the exchange rate service';return error_info
    else:
        result_error=has_error(result);return result_error
#Test is_currency
#It pass if result is not blank
def test_is_currency():
    assert (is_currency('USD', 'EUR', 22.2)=='')
#Get the value
#The response
def get_from(json_str):
    try:
        if type(json_str)==str:
            res=json.loads(json_str)
            return res['from']
        else:
            return json_str['from']
    except:
        return 'exception'
#Test get_from
#It pass if result is not blank
def test_get_from():
    assert (get_from('{"from": "3.1 United States Dollars", "to": "2.5980945 Euros", "success": true, "error": ""}') != '')
#Get the value of currency
#The response
def get_to(json_str):
    try:
        if type(json_str)==str:
            res=json.loads(json_str)
            return res['to']
        else:
            return json_str['to']
    except:
        return 'exception'
#Test get_to
#It pass if result is not blank
def test_get_to():
    assert (get_to('{"from": "3.1 United States Dollars", "to": "2.5980945 Euros", "success": true, "error": ""}') != '')
#currency exchange and will return the value
def exchange(curfrom, curto, amofrom):
    validate_result=is_currency(curfrom, curto, amofrom)
    if validate_result!='':
    	return validate_result
    result=re(curfrom, curto, amofrom)
    return get_to(result)
#TEST ALL FUNCTION
def test_all():
    print("test all")
    test_current_response()
    test_has_error()
    test_is_currency()
    test_get_from()
    test_get_to()
    print('is passed')
print(exchange('USD', 'EUR', 20.1))
