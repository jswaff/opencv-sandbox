import os
import numpy as np
import cv2



###### saving image descriptors to file
def create_descriptors(folder):
    feature_detector = cv2.xfeatures2d.SIFT_create()
    files = []
    for (dirpath, dirnames, filenames) in os.walk(folder):
        files.extend(filenames)
    for f in files:
        create_descriptor(folder, f, feature_detector)

def create_descriptor(folder, image_path, feature_detector):
    if not image_path.endswith('png'):
        print('skipping %s', image_path)
        return

    print('reading %s', image_path)
    img = cv2.imread(os.path.join(folder, image_path),
                     cv2.IMREAD_GRAYSCALE)
    keypoints, descriptors = feature_detector.detectAndCompute(img, None)
    descriptor_file = image_path.replace('png', 'npy')
    np.save(os.path.join(folder, descriptor_file), descriptors)

folder = './images/tattoos'
create_descriptors(folder)


#### scanning for matches
query = cv2.imread(os.path.join(folder, 'query.png'), cv2.IMREAD_GRAYSCALE)

# create files, images, descriptors globals
files = []
images = []
descriptors = []
for (dirpath, dirnames, filenames) in os.walk(folder):
    files.extend(filenames)
    for f in files:
        if f.endswith('npy') and f != 'query.npy':
            descriptors.append(f)
print(descriptors)


# create the SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# perform SIFT feature detection and description on the query image
query_kp, query_ds = sift.detectAndCompute(query, None)

# define FLANN based matching parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

# create the FLANN matcher
flann = cv2.FlannBasedMatcher(index_params, search_params)

MIN_NUM_GOOD_MATCHES = 10

greatest_num_good_matches = 0
prime_suspect = None

print('>> Initiating picture scan...')
for d in descriptors:
    print('----- analyzing %s for matches -----' % d)
    matches = flann.knnMatch(query_ds, np.load(os.path.join(folder,d)), k=2)
    good_matches = []
    for m,n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)
    num_good_matches = len(good_matches)
    name = d.replace('.npy', '').upper()
    if num_good_matches >= MIN_NUM_GOOD_MATCHES:
        print('%s is a suspect! (%d matches)' % (name, num_good_matches))
        if num_good_matches > greatest_num_good_matches:
            greatest_num_good_matches = num_good_matches
            prime_suspect = name
    else:
        print('%s is NOT a suspect. (%d matches)' % (name, num_good_matches))

if prime_suspect is not None:
    print('Prime suspect is %s.' % prime_suspect)
else:
    print('There is no suspect.')
