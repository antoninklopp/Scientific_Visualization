# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
import sys
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1128, 758]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.99999999998727, 46.45, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [2.16261017317024, 46.3371612595104, 64.2005781312117]
renderView1.CameraFocalPoint = [2.16261017317024, 46.3371612595104, 0.0]
renderView1.CameraParallelScale = 11.281891230701355

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
meteonc = NetCDFReader(FileName=[sys.argv[1]])
meteonc.Dimensions = '(latitude, longitude)'
meteonc.SphericalCoordinates = 0
meteonc.ReplaceFillValueWithNan = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=meteonc)
calculator1.Function = 'iHat*UGRD_10maboveground+jHat*VGRD_10maboveground'

# create a new 'Contour'
contour3 = Contour(Input=calculator1)
contour3.ContourBy = ['POINTS', 'TMP_2maboveground']
contour3.Isosurfaces = [295.0]
contour3.PointMergeMethod = 'Uniform Binning'

# create a new 'Contour'
contour6 = Contour(Input=calculator1)
contour6.ContourBy = ['POINTS', 'TMP_2maboveground']
contour6.Isosurfaces = [270.0]
contour6.PointMergeMethod = 'Uniform Binning'

# create a new 'Contour'
contour7 = Contour(Input=calculator1)
contour7.ContourBy = ['POINTS', 'TMP_2maboveground']
contour7.Isosurfaces = [265.0]
contour7.PointMergeMethod = 'Uniform Binning'

# create a new 'Contour'
contour2 = Contour(Input=calculator1)
contour2.ContourBy = ['POINTS', 'TMP_2maboveground']
contour2.Isosurfaces = [290.0]
contour2.PointMergeMethod = 'Uniform Binning'

# create a new 'Contour'
contour1 = Contour(Input=calculator1)
contour1.ContourBy = ['POINTS', 'TMP_2maboveground']
contour1.Isosurfaces = [285.0]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'RH_2maboveground']
glyph1.Vectors = ['POINTS', 'Result']
glyph1.ScaleFactor = 0.3
glyph1.GlyphTransform = 'Transform2'

# create a new 'Contour'
contour5 = Contour(Input=calculator1)
contour5.ContourBy = ['POINTS', 'TMP_2maboveground']
contour5.Isosurfaces = [275.0]
contour5.PointMergeMethod = 'Uniform Binning'

# create a new 'Contour'
contour4 = Contour(Input=calculator1)
contour4.ContourBy = ['POINTS', 'TMP_2maboveground']
contour4.Isosurfaces = [280.0]
contour4.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'TMP2maboveground'
tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
tMP2mabovegroundLUT.RGBPoints = [258.464172363281, 1.0, 1.0, 1.0, 299.37823486328125, 1.0, 1.0, 1.0]
tMP2mabovegroundLUT.NanColor = [1.0, 1.0, 1.0]
tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP2maboveground'
tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
tMP2mabovegroundPWF.Points = [258.464172363281, 1.0, 0.5, 0.0, 299.37823486328125, 1.0, 0.5, 0.0]
tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from meteonc
meteoncDisplay = Show(meteonc, renderView1)
# trace defaults for the display properties.
meteoncDisplay.Representation = 'Slice'
meteoncDisplay.ColorArrayName = ['POINTS', 'TMP_2maboveground']
meteoncDisplay.LookupTable = tMP2mabovegroundLUT
meteoncDisplay.ScalarOpacityUnitDistance = 0.194190573529865

# show data from contour1
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.Representation = 'Points'
contour1Display.AmbientColor = [1.0, 1.0, 0.0]
contour1Display.ColorArrayName = [None, '']

# show data from contour2
contour2Display = Show(contour2, renderView1)
# trace defaults for the display properties.
contour2Display.ColorArrayName = [None, '']
contour2Display.DiffuseColor = [1.0, 0.3333333333333333, 0.0]

# show data from contour3
contour3Display = Show(contour3, renderView1)
# trace defaults for the display properties.
contour3Display.ColorArrayName = [None, '']
contour3Display.DiffuseColor = [1.0, 0.0, 0.0]

# show data from contour4
contour4Display = Show(contour4, renderView1)
# trace defaults for the display properties.
contour4Display.ColorArrayName = [None, '']
contour4Display.DiffuseColor = [0.0, 1.0, 0.0]

# show data from contour5
contour5Display = Show(contour5, renderView1)
# trace defaults for the display properties.
contour5Display.ColorArrayName = [None, '']
contour5Display.DiffuseColor = [0.0, 0.6666666666666666, 1.0]

# show data from contour6
contour6Display = Show(contour6, renderView1)
# trace defaults for the display properties.
contour6Display.ColorArrayName = [None, '']
contour6Display.DiffuseColor = [0.0, 0.0, 1.0]

# show data from contour7
contour7Display = Show(contour7, renderView1)
# trace defaults for the display properties.
contour7Display.ColorArrayName = [None, '']
contour7Display.DiffuseColor = [0.6666666666666666, 0.0, 1.0]

output = "images/" + sys.argv[2] + ".png"
print("fichier sortie", output)
WriteImage(output)

import cv2

img = cv2.imread("images/" + sys.argv[2] + ".png", -1)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if sum(img[i, j]) > 250*4:
            img[i, j] = [0, 0, 0, 0]

print("outputing")

cv2.imwrite("images/" + sys.argv[2] + ".png", img)
