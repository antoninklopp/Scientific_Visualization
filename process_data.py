# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1128, 758]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.999999999987267, 46.45, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [2.138906879606897, 46.72871281947414, 64.20057813121173]
renderView1.CameraFocalPoint = [2.138906879606897, 46.72871281947414, 0.0]
renderView1.CameraParallelScale = 16.616332326949944
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
meteonc = NetCDFReader(FileName=['/user/2/klopptoa/Documents/3A/Scientific_Visualization/Projet/meteo.nc'])
meteonc.Dimensions = '(latitude, longitude)'
meteonc.SphericalCoordinates = 0
meteonc.ReplaceFillValueWithNan = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=meteonc)
calculator1.Function = 'UGRD_10maboveground*iHat+VGRD_10maboveground*jHat'

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator1,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'Result']
streamTracer1.MaximumStreamlineLength = 27.999999999974534

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-4.727182863406825, 37.49784994453761, -4.418687638008123e-14]
streamTracer1.SeedType.Point2 = [3.5172091907478062, 55.4277950066961, -2.5979218776228663e-14]

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'RH_2maboveground']
glyph1.Vectors = ['POINTS', 'Result']
glyph1.ScaleFactor = 0.24
glyph1.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'RH2maboveground'
rH2mabovegroundLUT = GetColorTransferFunction('RH2maboveground')
rH2mabovegroundLUT.RGBPoints = [17.933488845825195, 0.231373, 0.298039, 0.752941, 59.46473789215088, 0.865003, 0.865003, 0.865003, 100.99598693847656, 0.705882, 0.0156863, 0.14902]
rH2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RH2maboveground'
rH2mabovegroundPWF = GetOpacityTransferFunction('RH2maboveground')
rH2mabovegroundPWF.Points = [17.933488845825195, 0.0, 0.5, 0.0, 100.99598693847656, 1.0, 0.5, 0.0]
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
calculator1Display.ScalarOpacityUnitDistance = 0.1941905735298652

# show color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# show data from glyph1
glyph1Display = Show(glyph1, renderView1)
# trace defaults for the display properties.
glyph1Display.ColorArrayName = ['POINTS', 'RH_2maboveground']
glyph1Display.LookupTable = rH2mabovegroundLUT

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.ColorArrayName = [None, '']

# setup the color legend parameters for each legend in this view

# get color legend/bar for rH2mabovegroundLUT in view renderView1
rH2mabovegroundLUTColorBar = GetScalarBar(rH2mabovegroundLUT, renderView1)
rH2mabovegroundLUTColorBar.Title = 'RH_2maboveground'
rH2mabovegroundLUTColorBar.ComponentTitle = ''