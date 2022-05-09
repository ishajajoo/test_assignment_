import logging
import utilities.custom_logger as cl


class CopySave:
    """ Copy and save binary file from source to destination"""

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self):
        pass

    def copyfileobj(self, src, dst, buffer_size=1024 * 1024):

        """
        Copy a file from source to dest. source and dest
        must be file-like objects, i.e. any object with a read or
        write method, like for example StringIO.
        """

        while True:
            copy_buffer = src.read(buffer_size)
            self.log.info("Reading source file object")
            if not copy_buffer:
                break
            dst.write(copy_buffer)
            self.log.info("Writing source file object")

    def copyfile(self, src, dst):

        """
        Opening and copying the file content
        """
        self.log.info(src)
        self.file_name = src.split('/')[-1]
        self.log.info("Getting the source file name")
        try:
            with open(src, 'rb') as srce, open(dst + self.file_name, 'wb') as dest:
                self.log.info("Opening the source file {}".format(self.file_name))
                self.log.info("Creating and opening the destination file")
                self.copyfileobj(srce, dest)
                self.log.info("Copying the source file to destination file")
                self.log.info("Generating report")
        except OSError:
            self.log.error("Oops! cannot open {}".format(src))
