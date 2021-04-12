# This file is responsible to read the bitmap images
import os
import sys
import numpy as np

def read_image():
    """ This function reads the bitmap images

    :return: 2D representation of black and white bitmap images ( 2D numpy array)
    """

    input_image = open(os.path.join(os.getcwd(), "Input Images/image-5.bmp"), "rb")

    # size of image starting at offset 2, represented using 4 bytes
    # height and width of image starting offset 18, represented using 4 bytes each
    # number of bits per pixel starting offset 28, represented using 2 bytes


    input_image.seek(2)
    print("Image size in bytes: ", int.from_bytes(input_image.read(4), byteorder='little'))

    input_image.seek(18, 0)

    image_width = int.from_bytes(input_image.read(4), byteorder='little')
    image_height = int.from_bytes(input_image.read(4), byteorder='little')

    print("Image dimensions, width * height: ", image_width, "*", image_height)

    input_image.seek(28, 0)
    bytes_per_pixel = int.from_bytes(input_image.read(2), byteorder='little') // 8  
    print("Bytes per pixel is: ", bytes_per_pixel)


    input_image.seek(54, 0)  


    data_in_pixel_all_row = None

    data_in_pixel_all_row = np.array([[[each_byte for each_byte in reversed(input_image.read(bytes_per_pixel))]
                                       for i in range(image_width)] for j in range(image_height)], np.uint8)

    print("shape of the numpy array is: ", data_in_pixel_all_row.shape)

    return data_in_pixel_all_row


if __name__ =="__main__":

    read_image()
