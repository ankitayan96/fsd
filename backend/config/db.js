import mongoose from 'mongoose';

const connectDb = async () => {
  try {
    const conn = await mongoose.connect("mongodb+srv://ankit_ayan:BABBAN%40123@cluster0.qlyoe.mongodb.net/FSD?retryWrites=true&w=majority", {
      useUnifiedTopology: true,
      useNewUrlParser: true,
      useCreateIndex: true,
    });

    console.log(`MongoDB connected: ${conn.connection.host}`.cyan.underline);
  } catch (error) {
    console.error(`Error: ${error.message}`.red.underline.bold);
    process.exit(1);
  }
};

export default connectDb;
