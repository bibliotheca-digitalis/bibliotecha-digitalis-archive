# Bibliotheca Digitalis Archive

This is the GitHub repo for all the files in the Bibliotheca Digitalis Archive.
The archive is a collection of books, articles, transcripts and other
documents that are related to the Bibliotheca Digitalis project. The archive is
a work in progress and will be updated as the project progresses.

## Channel Avatar

![Channel Avatar](./avatar.jpg)

## Channel Banner

![Channel Banner](./banner.jpg)

## Channel Description

```
Hello.

I am a semi-automated YouTube Channel. I harvest videos from influential YouTube Channels and preserve them. All videos are downloaded, transcribed and uploaded to this channel. This is done using Whisper AI (extracting transcript) and Coqui TTS (text to speech) and ffmpeg (video generation). I hope you enjoy my content. I will be asking for suggestion to direct what channels I preserve next! 

Please be patient while I improve the audio quality and transcription performance! 

Project files:
https://github.com/bibliotheca-digitalis/bibliotheca-digitalis-archive

Content retrieved from other authors retain their original copyright and trademarks. Where applicable, any material generated using Whisper AI, Coqui TTS, ffmpeg, etc. is licensed under Creative Commons Zero v1.0 Universal. You have the "the right to reproduce, adapt, distribute, perform, display, communicate, and translate a Work." This also includes commercial activity, like reuploading, monetizing and selling.
```

## Tools Used

### AI Tools

- [Whisper AI](https://github.com/openai/whisper)
- [Coqui TTS](https://github.com/coqui-ai/TTS)

### Utilities

- [ffmpeg](https://ffmpeg.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

### Whisper Model Selection

- medium.en

#### Model Selection Philosophy

The medium.en model was selected because it is the largest model for English
related transcription. While the large model was used initially, it was found to
be too demanding, timewise and computationally as well. The medium model was
selected because it was explicitly trained on English and is not multilingual.

Moving forward, when transcribing other languages, discretion will have to be
exercised as to which model is the most appropriate for this use case. The
trade-off between transcribing fidelity and computational cost will be taken
into account.

## Channel Preservation Process

While there are many criteria that may steer the selection of a channel to
preserve, the main points are as follow:

- The channel is influential in the YouTube community
- The channel is widely discussed in the YouTube community
- The channel is emblematic of larger trends in the YouTube community
- The channel is at risk of being flagged for deletion
- The channel is at risk of being deleted

Out of these criteria, the most important is the first one and the last one.
While the first is obvious, the latter may motivate last minute efforts,
specially when a channel is embroiled in controversy.

## How to contribute

TODO

## Outstanding Issues TODO

- [ ] Add a channel TODO list
- [ ] Add synced subtitles to videos
