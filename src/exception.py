import sys
import logging

def error_message_detail(error, error_detail:sys):
    _, _, err = error_detail.exc_info()
    file_name = err.tb_frame.f_code.co_filename
    line_no = err.tb_lineno
    error_message = f"Error occured in python script {file_name}, line {line_no}: [{str(error)}]"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e, sys) 
    