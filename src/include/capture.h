#ifndef CAPTURE_H /* include guard */
#define CAPTURE_H


#include "log.h"
#include "configparser.h"

#include <stdio.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <time.h>
//#include <sqlite3.h>

#include <imp_audio.h>
#include <imp_log.h>
#include <imp_common.h>
#include <imp_osd.h>
#include <imp_framesource.h>
#include <imp_isp.h>
#include <imp_system.h>
#include <imp_encoder.h>
#include <imp/imp_ivs.h>
#include <imp/imp_ivs_move.h>

#include <linux/videodev2.h>
#include <h264_stream.h>
#include <cJSON.h>
#include <alsa/asoundlib.h>


//#define SENSOR_NAME				"jxf22"
#define SENSOR_CUBS_TYPE        TX_SENSOR_CONTROL_INTERFACE_I2C
#define SENSOR_I2C_ADDR			0x40
#define SENSOR_WIDTH			1920
#define SENSOR_HEIGHT			1080
#define CHN0_EN                 1
#define CHN1_EN                 1
#define CROP_EN					1

#define SENSOR_FRAME_RATE_NUM		25
#define SENSOR_FRAME_RATE_DEN		1

#define SENSOR_WIDTH_SECOND			1920
#define SENSOR_HEIGHT_SECOND		1080

#define OSD_REGION_WIDTH			16
#define OSD_REGION_HEIGHT			34

#define MAX_STREAMS				2

#define SENSOR_NAME_MAX_LENGTH	50

#define NIGHT_VISION_FILE_BUFFER_SIZE  8
#define NIGHT_VISION_FILE    "/tmp/night_vision_enabled"

#define LOG_ROTATE_SIGNAL	SIGUSR1
#define DEFAULT_LOGFILE 	"/var/log/videocapture.log"

int initialize_sensor(IMPSensorInfo *sensor_info);
int initialize_audio();
int configure_video_tuning_parameters(CameraConfig *camera_config);
int create_encoding_group(int group_id);
int setup_encoding_engine(FrameSource* frame_source, EncoderSetting* encoder_setting);
int output_v4l2_frames(EncoderSetting *encoder_setting);
int sensor_cleanup(IMPSensorInfo* sensor_info);
void hexdump(const char * desc, const void * addr, const int len);
void *produce_frames(void *ptr);
void *audio_thread_entry_start(void *audio_thread_params);
void *timestamp_osd_entry_start(void *timestamp_osd_thread_params);
void *night_vision_entry_start(void *night_vision_thread_params);
//void *real_time_configuration_start(void *params);
void print_stream_settings(StreamSettings *stream_settings);
void print_channel_attributes(IMPFSChnAttr *attr);
void print_encoder_channel_attributes(IMPEncoderCHNAttr *attr);
//int sql_camera_profile_callback(void *, int, char **, char **);

#endif /* CAPTURE_H */
