#ifndef __VISIONFEATUREPRINT_ENUMS_H
#define __VISIONFEATUREPRINT_ENUMS_H
enum MLVisionFeaturePrintVisionFeaturePrintType: int {
    MLVisionFeaturePrintVisionFeaturePrintType_scene = 20,
    MLVisionFeaturePrintVisionFeaturePrintType_objects = 21,
    MLVisionFeaturePrintVisionFeaturePrintType_NOT_SET = 0,
};

__attribute__((__unused__))
static const char * MLVisionFeaturePrintVisionFeaturePrintType_Name(MLVisionFeaturePrintVisionFeaturePrintType x) {
    switch (x) {
        case MLVisionFeaturePrintVisionFeaturePrintType_scene:
            return "MLVisionFeaturePrintVisionFeaturePrintType_scene";
        case MLVisionFeaturePrintVisionFeaturePrintType_objects:
            return "MLVisionFeaturePrintVisionFeaturePrintType_objects";
        case MLVisionFeaturePrintVisionFeaturePrintType_NOT_SET:
            return "INVALID";
    }
    return "INVALID";
}

enum MLSceneVersion: int {
    MLSceneVersionSCENE_VERSION_INVALID = 0,
    MLSceneVersionSCENE_VERSION_1 = 1,
    MLSceneVersionSCENE_VERSION_2 = 2,
};

enum MLObjectsVersion: int {
    MLObjectsVersionOBJECTS_VERSION_INVALID = 0,
    MLObjectsVersionOBJECTS_VERSION_1 = 1,
};

#endif
