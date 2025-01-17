from driver import initialize_default_driver
from tenff import tenff_automate

if __name__ == '__main__':
    my_driver = initialize_default_driver()
    tenff_automate(my_driver)
