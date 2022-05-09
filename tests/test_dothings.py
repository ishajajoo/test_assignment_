from file_copy.dothings import CopySave
import allure
import pytest
import os


class Test_do_nothings:
    """ This class tends to test the binary file copy feature"""

    dothings = CopySave()

    @allure.story('Story 1')
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_copy_binary_file(self, source_destination):
        """ Positive case: copy binary file"""
        self.dothings.copyfile(source_destination[1], source_destination[2])

    @allure.story('Story 2')
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_validate_file_buffer_size(self, source_destination):
        """ Positive case: check for buffer size(content size)"""
        self.dothings.copyfile(source_destination[1], source_destination[2])

    @allure.story('Story 3')
    @pytest.mark.smoke
    @pytest.mark.negative
    def test_is_file_name_empty(self, source_destination):
        """ Negative case: check for empty source file name in path"""
        assert source_destination[1] is not None, "Empty source file name"

    @allure.story('Story 4')
    @pytest.mark.smoke
    def test_source_destination_size(self, source_destination):
        """ Verify file size is same for both files"""
        self.dothings.copyfile(source_destination[1], source_destination[2])
        source_file_size = os.path.getsize(source_destination[1])
        destination_file_size = os.path.getsize(source_destination[2] + self.dothings.file_name)
        assert source_file_size == destination_file_size, "Mismatch in source and destination file size"

    @allure.story('Story 5')
    @pytest.mark.smoke
    def test_source_destination_name(self, source_destination):
        """ Verify file size is same for both files"""
        self.dothings.copyfile(source_destination[1], source_destination[2])
        assert self.dothings.file_name == source_destination[2], "File sizes mismatch"

    @allure.story('Story 6')
    @pytest.mark.smoke
    def test_source_destination_content(self, source_destination):
        """ Verify file size is same for both files"""
        self.dothings.copyfile(source_destination[1], source_destination[2])
        assert open("source_destination[1]", 'rb').read() == open("source_destination[2] + self.dothings.file_name", "rb").read(), "Mismatch in file content"

    @allure.story('Story 7')
    @pytest.mark.smoke
    def test_source_destination_file_type(self, source_destination):
        """ Verify file extension is same for both files"""
        self.dothings.copyfile(source_destination[1], source_destination[2])
        assert os.path.splitext(source_destination[1])[2] == os.path.splitext(source_destination[2] + self.dothings.file_name)[2], "Mismatch in file type"

    @allure.story('Story 8')
    @pytest.mark.smoke
    @pytest.mark.negative
    def test_corrupt_file(self, source_destination):
        """ Verify file extension is same for both files"""
        self.dothings.copyfile(source_destination[1], source_destination[2])
