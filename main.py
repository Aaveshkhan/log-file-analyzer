from prettytable import PrettyTable, ALL

log_file_location = '/var/log/nginx/access.log'
log_data = {}


def ip_generating_highest_status_code_count_of(code: int):
    request_code_tally = {}
    highest_code_count_ip = None
    highest_code_count = 0

    for ip, request_data_list in log_data.items():
        for request_data in request_data_list:
            if request_data['STATUS CODE'] == str(code):
                if ip not in request_code_tally:
                    request_code_tally[ip] = 0
                request_code_tally[ip] += 1

    for ip, code_count in request_code_tally.items():
        if code_count > highest_code_count:
            highest_code_count = code_count
            highest_code_count_ip = ip

    return highest_code_count_ip


def get_most_requested_page():
    page_request_tally = {}
    most_requested_page = None
    most_requested_page_requests = 0

    for request_data_list in log_data.values():
        for request_data in request_data_list:
            page = request_data['PATH']
            if page not in page_request_tally:
                page_request_tally[page] = 0
            page_request_tally[page] += 1

    for page, request_count in page_request_tally.items():
        if request_count > most_requested_page_requests:
            most_requested_page = page
            most_requested_page_requests = request_count

    return most_requested_page


def ip_generating_highest_request_for_method(method: str):
    method_tally = {}
    highest_method_count_ip = None
    highest_method_count = 0

    for ip, request_data_list in log_data.items():
        for request_data in request_data_list:
            if request_data['METHOD'] == method:
                if ip not in method_tally:
                    method_tally[ip] = 0
                method_tally[ip] += 1

    for ip, method_count in method_tally.items():
        if method_count > highest_method_count:
            highest_method_count_ip = ip
            highest_method_count = method_count

    return highest_method_count_ip


def get_status_code_count(code: int):
    status_code_count = 0

    for request_data_list in log_data.values():
        for request_data in request_data_list:
            if request_data['STATUS CODE'] == str(code):
                status_code_count += 1

    return status_code_count


with open(log_file_location, 'r') as logfile:
    for log in logfile:
        log_split = log.split(" ")
        ip_address = log_split[0]
        method = log_split[5][1:]
        path = log_split[6]
        status_code = log_split[8]
        if ip_address not in log_data:
            log_data[ip_address] = []
        log_data[ip_address].append({'STATUS CODE': status_code, 'METHOD': method, 'PATH': path})

CODE_TO_CHECK = 404
METHOD_TO_CHECK = 'GET'

table = PrettyTable()
table.header = False
table.align = 'l'
table.hrules = ALL

table_rows = [
    ["Log File Location", log_file_location],
    [f"I.P. generating the highest {CODE_TO_CHECK} requests",
     ip_generating_highest_status_code_count_of(CODE_TO_CHECK)],
    [f"Count of {CODE_TO_CHECK} requests made", get_status_code_count(CODE_TO_CHECK)],
    [f"I.P. generating the highest number of {METHOD_TO_CHECK} requests",
     ip_generating_highest_request_for_method(METHOD_TO_CHECK)],
    [f"Most requested page", get_most_requested_page()]
]
table.add_rows(table_rows)

print("*" * 82)
print(' ' * 31 + "Log Analysis Summary" + ' ' * 31)
print("*" * 82)
print(table)
print("*" * 82)

