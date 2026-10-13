import AVFoundation
import AppKit
// fxall movie outdir step width — every `step` seconds, a small PNG named by its time in ms
let a = CommandLine.arguments
let asset = AVURLAsset(url: URL(fileURLWithPath: a[1]))
let gen = AVAssetImageGenerator(asset: asset)
gen.requestedTimeToleranceBefore = .zero; gen.requestedTimeToleranceAfter = .zero
gen.maximumSize = CGSize(width: Double(a[4])!, height: 10000)
let dur = CMTimeGetSeconds(asset.duration); let step = Double(a[3])!
var t = 0.0
while t < dur {
    if let cg = try? gen.copyCGImage(at: CMTime(seconds: t, preferredTimescale: 600), actualTime: nil) {
        let rep = NSBitmapImageRep(cgImage: cg)
        try? rep.representation(using: .png, properties: [:])?.write(to: URL(fileURLWithPath: "\(a[2])/\(String(format: "%07d", Int(t * 1000))).png"))
    }
    t += step
}
