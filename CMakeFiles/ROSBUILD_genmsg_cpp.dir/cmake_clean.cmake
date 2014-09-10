FILE(REMOVE_RECURSE
  "src/raven_2/msg"
  "msg_gen"
  "msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "msg_gen/cpp/include/raven_2/raven_state.h"
  "msg_gen/cpp/include/raven_2/raven_jointmove.h"
  "msg_gen/cpp/include/raven_2/raven_automove.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
