import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping

def trash_model():
    datagambar = 'Datasets/datasets'

    train_data_dir = datagambar
    batch_size = 128
    target_size = (180,180)
    validation_split = 0.2

    train= tf.keras.preprocessing.image_dataset_from_directory(
        train_data_dir,
        validation_split=validation_split,
        subset="training",
        seed=50,                                                         # de 100 para 50
        image_size=target_size,
        batch_size=batch_size,
    )
    validation= tf.keras.preprocessing.image_dataset_from_directory(
        train_data_dir,
        validation_split=validation_split,
        subset="validation",
        seed=100,                                                         # de 200 para 100
        image_size=target_size,
        batch_size=batch_size,
    )

    class_names = train.class_names #Have 12 Class

    model = tf.keras.models.Sequential([
        tf.keras.layers.Rescaling(1./255, input_shape=(180, 180, 3)),
        tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(len(class_names), activation='softmax')
    ])

    model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Callbacks
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    # Melatih model
    history = model.fit(train, validation_data=validation, epochs=20, callbacks=[early_stopping])

if __name__ == '__main__':
    model, class_df = trash_model()
    model.save("trash_model.h5")