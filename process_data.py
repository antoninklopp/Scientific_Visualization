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
renderView1.CameraPosition = [1.44540518280946, 45.2092844699121, 64.2005781312117]
renderView1.CameraFocalPoint = [1.44540518280946, 45.2092844699121, 0.0]
renderView1.CameraParallelScale = 11.3491785581244
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
meteonc = NetCDFReader(FileName=['/user/2/.base/klopptoa/home/Documents/3A/Scientific_Visualization/Projet/meteo.nc'])
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

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator1,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'Result']
streamTracer1.MaximumStreamlineLength = 27.999999999974534

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-5.1425807656715286, 38.21868149180743, 0.0]
streamTracer1.SeedType.Point2 = [5.908514052512984, 55.4898351864761, 0.0]

# create a new 'Contour'
contour1 = Contour(Input=calculator1)
contour1.ContourBy = ['POINTS', 'RH_2maboveground']
contour1.Isosurfaces = [59.4647378921509]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'RH2maboveground'
rH2mabovegroundLUT = GetColorTransferFunction('RH2maboveground')
rH2mabovegroundLUT.RGBPoints = [17.933488845825195, 0.231373, 0.298039, 0.752941, 59.46473789215089, 0.865003, 0.865003, 0.865003, 100.995986938477, 0.705882, 0.0156863, 0.14902]
rH2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RH2maboveground'
rH2mabovegroundPWF = GetOpacityTransferFunction('RH2maboveground')
rH2mabovegroundPWF.Points = [17.933488845825195, 0.0, 0.5, 0.0, 100.995986938477, 1.0, 0.5, 0.0]
rH2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.Representation = 'Slice'
calculator1Display.ColorArrayName = ['POINTS', 'RH_2maboveground']
calculator1Display.LookupTable = rH2mabovegroundLUT
calculator1Display.ScalarOpacityUnitDistance = 0.194190573529865

# show color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# show data from glyph1
glyph1Display = Show(glyph1, renderView1)
# trace defaults for the display properties.
glyph1Display.ColorArrayName = ['POINTS', 'RH_2maboveground']
glyph1Display.LookupTable = rH2mabovegroundLUT

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# show data from contour1
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.ColorArrayName = [None, '']

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface With Edges'
streamTracer1Display.ColorArrayName = ['POINTS', 'RH_2maboveground']
streamTracer1Display.LookupTable = rH2mabovegroundLUT
streamTracer1Display.EdgeColor = [1.0, 1.0, 1.0]

# show color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for rH2mabovegroundLUT in view renderView1
rH2mabovegroundLUTColorBar = GetScalarBar(rH2mabovegroundLUT, renderView1)
rH2mabovegroundLUTColorBar.Title = 'RH_2maboveground'
rH2mabovegroundLUTColorBar.ComponentTitle = ''

output = "images/" + sys.argv[2] + ".png"
print("fichier sortie", output)
WriteImage(output)
