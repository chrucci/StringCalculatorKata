class InvalidAddnedException(Exception):

    def __init__(self, invalid_nums):
        nums = ",".join(invalid_nums)
        self.message = "Negative numbers are not allowed.  You included '" + nums + "'"
        super().__init__(self.message)
