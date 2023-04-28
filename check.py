# Import required modules
import cv2
import numpy as np

CHECKERBOARD = (6, 8)

criteria = (cv2.TERM_CRITERIA_EPS +
			cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

threedpoints = []
twodpoints = []

objectp3d = np.zeros((1, CHECKERBOARD[0]
					* CHECKERBOARD[1],
					3), np.float32)

objectp3d[0, :, :2] = np.mgrid[0:CHECKERBOARD[0],
							0:CHECKERBOARD[1]].T.reshape(-1, 2)

# ----------------------------------------------------------
# NO
# file = "CheckBoard/dis1.jpg"
# file = "CheckBoard/dis2.png"
# file = "CheckBoard/dis7.png"
# file = "CheckBoard/dis5.jpg"
# file = "CheckBoard\dis9.jpg"
# ----------------------------------------------------------


# file = "CheckBoard\\checkboard_from_pdf.png"
# file = "CheckBoard/dis3.png"
file = "CheckBoard/dis4.png"
# file = "CheckBoard\dis8.jpg"
# file = 
image = cv2.imread(file)

if image is None:
    print("Can not find image")
else:
    grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(grayColor, CHECKERBOARD,cv2.CALIB_CB_ADAPTIVE_THRESH+ cv2.CALIB_CB_FAST_CHECK +cv2.CALIB_CB_NORMALIZE_IMAGE)

print(ret)
if ret == True:
    threedpoints.append(objectp3d)

    corners2 = cv2.cornerSubPix(
        grayColor, corners, (11, 11), (-1, -1), criteria)
    twodpoints.append(corners2)
    image = cv2.drawChessboardCorners(image,
                                    CHECKERBOARD,
                                    corners2, ret)

cv2.imshow('img', image)
cv2.waitKey(0)

cv2.destroyAllWindows()

h, w = image.shape[:2]

ret, matrix, distortion, r_vecs, t_vecs = cv2.calibrateCamera(
	threedpoints, twodpoints, grayColor.shape[::-1], None, None)

# Displaying required output
print(" Camera matrix:")
print(matrix)

print("\n Distortion coefficient:")
print(distortion)

print("\n Rotation Vectors:")
print(r_vecs)

print("\n Translation Vectors:")
print(t_vecs)

# file = "CheckBoard/dis8.jpg"
img = cv2.imread(file)

h,w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(matrix,distortion,(w,h),1,(w,h))

# undistort
dst = cv2.undistort(img, matrix, distortion, None, newcameramtx)

# crop the image
x,y,w,h = roi

dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png',dst)

cv2.imshow('img', dst)
cv2.waitKey(0)

mapx,mapy = cv2.initUndistortRectifyMap(matrix,distortion,None,newcameramtx,(w,h),5)
dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult2.png',dst)

cv2.imshow('img', dst)
cv2.waitKey(0)

mean_error = 0
for i in range(len(threedpoints)):
    imgPoint = twodpoints[i]
    objPoint = threedpoints[i]
    rvecs = r_vecs[i]
    tvecs = t_vecs[i]
    projPoints, _ = cv2.projectPoints(objPoint, rvecs, tvecs, matrix, distortion)
    error = cv2.norm(imgPoint, projPoints, cv2.NORM_L2) / len(projPoints)
    mean_error += error

print("total error: {}".format(mean_error / len(threedpoints)))


