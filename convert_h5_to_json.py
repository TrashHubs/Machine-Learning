import tensorflowjs as tfjs
from tensorflow.keras.models import load_model


def convert_keras_to_tfjs(h5_model_path, tfjs_target_dir):
    model = load_model(h5_model_path)
    tfjs.converters.save_keras_model(model, tfjs_target_dir)
    print(f'Model converted and saved to {tfjs_target_dir}')


if __name__ == "__main__":
    h5_model_path = 'nad_trash_model.h5'
    tfjs_target_dir = 'json-model'
    convert_keras_to_tfjs(h5_model_path, tfjs_target_dir)
