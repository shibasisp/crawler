from html_lib import HtmlLib
from config import write_to_excel


class Scraper:

    def __init__(self):
        self.output = []
        self.html_lib = HtmlLib()
        self.current_page_index = -1
        self.total_items = sum([len(page_items) for page_items in self.output])

    def scrape(self, page_source, new_page=False):

        if new_page or self.current_page_index is -1:
            self.current_page_index += 1
            self.output.append([])

        self.output[self.current_page_index] += self.html_lib.elements_attribute_map(page_source, from_index=len(self.output[self.current_page_index]))

        self.total_items = sum([len(page_items) for page_items in self.output])

    def process_output(self):

        concatenated_output = []
        for result in self.output:
            concatenated_output += result
        print len(concatenated_output)
        all_keys = []
        result_keys = [result.keys() for result in concatenated_output]

        for result_key in result_keys:

            for key in result_key:
                if key not in all_keys:
                    all_keys.append(key)

        all_keys = set(all_keys)

        for result in concatenated_output:
            for key in all_keys:
                if key not in result:
                    result[key] = ''

        for output in concatenated_output:

            for key in output:
                print key,
                print ": ",
                print output[key],

            print ""

        write_to_excel(concatenated_output, all_keys)
