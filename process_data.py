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
renderView1.ViewSize = [925, 566]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.99999999998727, 46.45, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [2.017283819121423, 46.31884724634661, 64.2005781312117]
renderView1.CameraFocalPoint = [2.017283819121423, 46.31884724634661, 0.0]
renderView1.CameraParallelScale = 8.656775699241452

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

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'RH_2maboveground']
glyph1.Vectors = ['POINTS', 'Result']
glyph1.ScaleFactor = 0.3
glyph1.GlyphTransform = 'Transform2'

# create a new 'Contour'
contour1 = Contour(Input=calculator1)
contour1.ContourBy = ['POINTS', 'TMP_2maboveground']
contour1.Isosurfaces = [285.0]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator1,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'Result']
streamTracer1.MaximumStreamlineLength = 27.9999999999745

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-5.14258076567153, 38.2186814918074, 0.0]
streamTracer1.SeedType.Point2 = [5.90851405251298, 55.4898351864761, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'TMP2maboveground'
tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
tMP2mabovegroundLUT.RGBPoints = [258.464172363281, 1.0, 0.0, 1.0, 271.35830954042706, 0.666666666666667, 0.0, 1.0, 273.58996582031205, 0.0, 0.0, 0.498039215686275, 276.3175806474781, 0.0, 0.396078431372549, 0.886274509803922, 278.4252624511721, 0.43921568627451, 0.803921568627451, 1.0, 278.5492553710941, 0.36078431372549, 1.0, 0.756862745098039, 280.7809448242191, 0.0, 1.0, 0.0, 285.86419677734415, 1.0, 1.0, 0.0, 289.2117004394532, 1.0, 0.666666666666667, 0.0, 294.04699707031216, 1.0, 0.0, 0.0, 299.37823486328125, 0.666666666666667, 0.0, 0.0]
tMP2mabovegroundLUT.NanColor = [1.0, 1.0, 1.0]
tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP2maboveground'
tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
tMP2mabovegroundPWF.Points = [258.464172363281, 1.0, 0.5, 0.0, 299.37823486328125, 1.0, 0.5, 0.0]
tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# get color transfer function/color map for 'RH2maboveground'
rH2mabovegroundLUT = GetColorTransferFunction('RH2maboveground')
rH2mabovegroundLUT.RGBPoints = [17.9334888458252, 0.231373, 0.298039, 0.752941, 59.4647378921509, 0.865003, 0.865003, 0.865003, 100.995986938477, 0.705882, 0.0156863, 0.14902]
rH2mabovegroundLUT.NanColor = [1.0, 1.0, 1.0]
rH2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RH2maboveground'
rH2mabovegroundPWF = GetOpacityTransferFunction('RH2maboveground')
rH2mabovegroundPWF.Points = [17.9334888458252, 0.0, 0.5, 0.0, 100.995986938477, 1.0, 0.5, 0.0]
rH2mabovegroundPWF.ScalarRangeInitialized = 1

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
contour1Display.AmbientColor = [0.0, 0.0, 0.0]
contour1Display.ColorArrayName = [None, '']

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface With Edges'
streamTracer1Display.ColorArrayName = ['POINTS', 'RH_2maboveground']
streamTracer1Display.LookupTable = rH2mabovegroundLUT
streamTracer1Display.EdgeColor = [1.0, 1.0, 1.0]

output = "images/" + sys.argv[2] + ".png"
print("fichier sortie", output)
WriteImage(output)
