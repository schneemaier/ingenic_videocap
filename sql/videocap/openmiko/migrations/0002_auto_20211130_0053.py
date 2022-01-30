# Generated by Django 3.2.9 on 2021-11-30 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("openmiko", "0001_initial"),
    ]

    def forward(apps, schema_editor):
        AeStrategy = apps.get_model("openmiko", "AeStrategy")
        ae_strategy, created = AeStrategy.objects.get_or_create(
            name="IMPISP_AE_STRATEGY_SPLIT_BALANCED", description="normal mode", enum=0
        )
        AeStrategy.objects.get_or_create(
            name="IMPISP_AE_STRATEGY_SPLIT_INTEGRATION_PRIORITY", description="", enum=1
        )
        AeStrategy.objects.get_or_create(
            name="IMPISP_AE_STRATEGY_BUTT", description="", enum=2
        )

        SceneMode = apps.get_model("openmiko", "SceneMode")
        scene_mode, created = SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_AUTO", description="auto mode", enum=0
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_BEACH_SNOW",
            description="beach and snow mode",
            enum=2,
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_CANDLE_LIGHT",
            description="candle light mode",
            enum=3,
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_DAWN_DUSK", description="dawn/dusk mode", enum=4
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_FALL_COLORS", description="fall colors mode", enum=5
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_FIREWORKS", description="fireworks mode", enum=6
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_LANDSCAPE", description="landscape mode", enum=7
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_NIGHT", description="night mode", enum=8
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_PARTY_INDOOR",
            description="indoor party mode",
            enum=9,
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_SPORTS", description="sports mode", enum=11
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_SUNSET", description="sunset mode", enum=12
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_TEXT", description="text mode", enum=13
        )
        SceneMode.objects.get_or_create(
            name="IMPISP_SCENE_MODE_NIGHT_PORTRAIT",
            description="night portrait mode",
            enum=14,
        )

        ColorfxMode = apps.get_model("openmiko", "ColorfxMode")
        color_fx_mode, created = ColorfxMode.objects.get_or_create(
            name="IMPISP_COLORFX_MODE_AUTO", description="auto mode", enum=0
        )
        color_fx_mode, created = ColorfxMode.objects.get_or_create(
            name="IMPISP_COLORFX_MODE_BW", description="black and white", enum=1
        )
        color_fx_mode, created = ColorfxMode.objects.get_or_create(
            name="IMPISP_COLORFX_MODE_SEPIA", description="sepia", enum=2
        )
        color_fx_mode, created = ColorfxMode.objects.get_or_create(
            name="IMPISP_COLORFX_MODE_NEGATIVE", description="negative", enum=3
        )
        color_fx_mode, created = ColorfxMode.objects.get_or_create(
            name="IMPISP_COLORFX_MODE_VIVID", description="vivid", enum=9
        )

        # Create the default camera profile
        CameraProfile = apps.get_model("openmiko", "CameraProfile")
        camera_profile = CameraProfile(
            ae_strategy=ae_strategy, scene_mode=scene_mode, color_fx_mode=color_fx_mode
        )
        camera_profile.save()

    def backward(apps, schema_editor):
        pass

    operations = [migrations.RunPython(forward, backward)]