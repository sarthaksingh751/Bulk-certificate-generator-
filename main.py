import os
import cv2

list_of_names = []

def delete_old_data():
    for i in os.listdir("generate_certificate/"):
        os.remove("generate_certificate/{}".format(i))


def cleanup_data():
    with open('names.txt') as f:  #open this tesxt file
        for line in f:
            list_of_names.append(line.strip())

#ADD NAMES
#SAVE IN JPG FORMATE
def generate_certificate():
    for index, name in enumerate(list_of_names):
        certificate_template_image = cv2.imread("certificate.jpg")                      #read image
        cv2.putText(certificate_template_image, name.strip(), (480, 521), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0,0 ), 5,cv2.LINE_AA)
        cv2.imwrite("generate_certificate/{}.jpg".format(name.strip()), certificate_template_image)
        print("generated{} / {}".format(index + 1, len(list_of_names)))

#DELETE OLD DATA
def main():
    delete_old_data()
    cleanup_data()
    generate_certificate()

if __name__ == '__main__':
    main()