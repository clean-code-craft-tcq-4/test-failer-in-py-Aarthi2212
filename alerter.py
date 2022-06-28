from alert import alert_in_celcius, call_network_alert
threshold = 200
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    status_code = 200
    # Return 500 if exceeds threshold. Assuming threshold of 200.
    if celcius > threshold:
        status_code = 500
    return status_code

# separated getting alert in celcius and network calling part and passing network communication as an argument make it more easy for prod code.
# alert check for values above threshold
celcius = alert_in_celcius(500.1)
alert_failure_count = call_network_alert(celcius, network_alert_stub)
celcius = alert_in_celcius(400.5)
alert_failure_count = call_network_alert(celcius, network_alert_stub)

# alert check for value below threshold
celcius = alert_in_celcius(303.6)
alert_failure_count = call_network_alert(celcius, network_alert_stub)

# alert check for value equal to threshold
celcius = alert_in_celcius(392)
alert_failure_count = call_network_alert(celcius, network_alert_stub)

# test to check alert_failure_count if it is incrementing for failures and not zero.
assert(alert_failure_count > 0)

# since we have two test values above threshold failure count should be 2.
assert(alert_failure_count == 2)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')