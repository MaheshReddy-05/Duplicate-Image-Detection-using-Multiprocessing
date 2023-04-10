import cv2
import numpy as np
import glob
import time
import concurrent.futures
import threading

from os import path


# setting up path
basepath = path.dirname(__file__)


# loading environment

# image_path = './images_in'
image_path = path.abspath(path.join(basepath, "../images_in", "duplicate.jpg")) # Image we are running these tests against.


"""
Multithreading
"""


original = cv2.imread(image_path) 


def find_duplicates(image_):
    duplicates = ''
    try:
        image_to_compare = cv2.imread(image_)
        if original.shape == image_to_compare.shape:

            difference = cv2.subtract(original, image_to_compare)
            b, g, r = cv2.split(difference)

            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                sift = cv2.SIFT_create()
                kp_1, desc_1 = sift.detectAndCompute(original, None)
                kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

                index_params = dict(algorithm=0, trees=5)
                search_params = dict()
                flann = cv2.FlannBasedMatcher(index_params, search_params)

                matches = flann.knnMatch(desc_1, desc_2, k=2)

                good_points = []
                for m, n in matches:
                    if m.distance < 0.6*n.distance:
                        good_points.append(m)

                number_keypoints = len(good_points)
                similarity = number_keypoints / min(len(kp_1), len(kp_2)) * 100
                # print(f"Number of keypoints matched: {number_keypoints}")
                # print(f"Similarity score: {similarity}%")
                if(similarity==100):
                    print(f'Duplicates Found: {image_path} is Duplicate of {image_}')

    except Exception as e:
        print('[!] {}'.format(e))

if __name__ == '__main__':
    

    def filebrowser(ext='', directory=''):
        """
        returns files with an extension
        """
        return [f for f in glob.glob(f"{directory}**/*{ext}", recursive=True)]

    image_dir = filebrowser(ext='.jpeg', directory='') 
    image_dir += filebrowser(ext='.jpg', directory='')
    image_dir += filebrowser(ext='png',directory='')
    image_dir += filebrowser(ext='gif',directory='')
    


    start_time = time.time()

    threads = []

    for image_ in image_dir:
        t = threading.Thread(target=find_duplicates, args=(image_,))
        t.daemon = False
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("--- %s seconds ---" % (time.time() - start_time))
    print('Program Executed Completely')

































# if __name__ == '__main__':
    
    # pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    # # Get the list of image paths
    # def filebrowser(ext='', directory=''):
    #     """
    #     returns files with an extension
    #     """
    #     return [f for f in glob.glob(f"{directory}**/*{ext}", recursive=True)]

    # image_dir = filebrowser(ext='.jpeg', directory='') 
    # image_dir += filebrowser(ext='.jpg', directory='')

    # start_time = time.time()

    # # Submit each image to the thread pool
    # results = [pool.submit(find_duplicates, image_) for image_ in image_dir]

    # # Wait for all the worker threads to complete
    # for result in concurrent.futures.as_completed(results):
    #         result.result()


    # print("--- %s seconds ---" % (time.time() - start_time))
    # print('Program Executed Completely')
























# if __name__ == '__main__':
    
#     pool = multiprocessing.ThreadPool(4)

#     # Get the list of image paths
#     def filebrowser(ext='', directory=''):
#         """
#         returns files with an extension
#         """
#         return [f for f in glob.glob(f"{directory}**/*{ext}", recursive=True)]

#     image_dir = filebrowser(ext='.jpeg', directory='') 
#     image_dir += filebrowser(ext='.jpg', directory='')

#     start_time = time.time()

#     # Submit each image to the process pool
#     results = [pool.apply_async(find_duplicates, args=(image_,)) for image_ in image_dir]

#     # Wait for all the worker processes to complete
#     for result in results:
#         result.wait()

#     print("--- %s seconds ---" % (time.time() - start_time))
#     print('Program Executed Completely')
